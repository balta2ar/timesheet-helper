if exists('g:timesheet_helper_plugin_loaded') || &cp
    finish
endif
let g:timesheet_helper_plugin_loaded = 1

let g:timesheet_helper_plugin_path = expand('<sfile>:p:h')

" To setup Python imports
call timesheet_helper#SetupPyImports()

" A command to call
command! -nargs=0 TimesheetHelperCommand call timesheet_helper#TimesheetHelperCommand()
command! -nargs=0 TimesheetHelperUpdateCurrentLine call timesheet_helper#TimesheetHelperUpdateCurrentLine()
