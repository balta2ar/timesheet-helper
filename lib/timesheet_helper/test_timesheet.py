import unittest
from timesheet import do_something, parse_line, borrow_time

PREV_LINE = '2018-05-23,10:50,12:00,bsw-reporting-dev,RT:111111,"general activity"'
RT_LINE = '2000-05-23,14:00,18:00,bsw-cm-wrong-queue,RT:222222,"investigating issues, pg_restore"'
JIRA_LINE = '2000-05-23,13:30,14:00,BSW_REPORTING_DEV-461,"code review, test"'


class TimesheetTestCase(unittest.TestCase):

    def test_doing_something(self):
        pass

    def test_update_rt_line(self):
        pass

    def test_update_jira_line(self):
        pass


if __name__ == '__main__':
    #unittest.main()
    print('TEST')
    # print(parse_line(RT_LINE))
    # print(parse_line(JIRA_LINE))
    print('PREV', PREV_LINE)
    print('NEW RT', str(borrow_time(RT_LINE, PREV_LINE)))
    print('NEW JIRA', str(borrow_time(JIRA_LINE, PREV_LINE)))
    print('DONE')
