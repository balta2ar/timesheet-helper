def do_something():
    print("Hello!")


import re
import csv
from time import localtime, strftime
from subprocess import check_output
FIRST_TIME_START = len('2018-01-25,')
SECOND_TIME_START = len('2018-01-25,16:20,')
QUEUE_START = len('2018-01-25,16:20,12:00,')


class RTLine:
    def __init__(self, parts):
        self.parts = parts
        self.date, self.start, self.end, self.queue, self.ticket, self.comment = parts

    def __str__(self):
        self.parts = self.date, self.start, self.end, self.queue, self.ticket, '"%s"' % self.comment
        return ','.join(self.parts)

class JIRALine:
    def __init__(self, parts):
        self.parts = parts
        self.date, self.start, self.end, self.ticket, self.comment = parts

    def __str__(self):
        self.parts = self.date, self.start, self.end, self.ticket, '"%s"' % self.comment
        return ','.join(self.parts)


def parse_line(line):
    parts = list(csv.reader([line]))[0]
    if len(parts) == 6:
        # RT line
        return RTLine(parts)
    elif len(parts) == 5:
        # JIRA line
        return JIRALine(parts)
    else:
        print('Unexpected number of columns in a line: "%s"' % line)
        return None


def get_queue(rt_ticket):
    # 1 rt_ticket, 2 description, 3 status, 4 owner, 5 queue, 6 updated
    output = check_output(['rt', rt_ticket]).decode('utf8')
    return output.split('\t')[4]

def get_ticket(line):
    return re.search(r'RT:?(\d\d\d\d\d\d)', line).group(1)

def current_time():
    return strftime("%H:%M", localtime())

def current_date():
    return strftime("%Y-%m-%d", localtime())

def extract_second_time(line):
    return line[SECOND_TIME_START:SECOND_TIME_START+5]

def put(line, timestamp, pos, end=None):
    L = len(timestamp) if end is None else end
    return line[:pos] + timestamp + line[pos + L:]

def borrow_time(current_line, previous_line):
    current_line = parse_line(current_line)
    previous_line = parse_line(previous_line)

    if isinstance(current_line, RTLine):
        correct_queue = get_queue(get_ticket(current_line.ticket))
        current_line.queue = correct_queue
    current_line.date = current_date()
    current_line.start = previous_line.end
    current_line.end = current_time()
    return current_line

    # line = put(current_line, current_date(), 0)
    # line = put(line, extract_second_time(previous_line), FIRST_TIME_START)
    # line = put(line, current_time(), SECOND_TIME_START)
    # correct_queue = get_queue(get_ticket(current_line))
    # line = put(line, correct_queue, QUEUE_START, current_line[QUEUE_START:].index(','))
    # return line

def update_current_timesheet_line():
    import vim
    current_line_number = int(vim.eval("line('.')"))
    current_line = vim.eval("getline(%d)" % current_line_number)
    previous_line = vim.eval("getline(%d)" % (current_line_number - 1))
    new_current_line = str(borrow_time(current_line, previous_line))
    vim.eval("setline(%d, '%s')" % (current_line_number, new_current_line))

