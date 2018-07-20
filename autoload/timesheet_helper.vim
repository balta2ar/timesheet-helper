function! timesheet_helper#TimesheetHelperCommand()
python3 << endpython3
import vim
from timesheet_helper import timesheet

timesheet.do_something()

endpython3
endfunction

function! timesheet_helper#TimesheetHelperUpdateCurrentLine()
python3 << endpython3
import vim
from timesheet_helper import timesheet

timesheet.update_current_timesheet_line()

endpython3
endfunction

function! timesheet_helper#SetupPyImports()
python3 << endpython3
import os
import sys
import vim

python_plugin_path_loaded = int(vim.eval('exists("g:timesheet_helper_plugin_path_loaded")'))

if python_plugin_path_loaded == 0:
    vim.command("let g:timesheet_helper_plugin_path_loaded=1")

    plugin_path = vim.eval("g:timesheet_helper_plugin_path")
    python_plugin_path = os.path.abspath('%s/../lib' % (plugin_path))
    sys.path.append(python_plugin_path)

endpython3
endfunction
