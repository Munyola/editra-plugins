

# Introduction #

This page contains a list of open TODO issues for a future version of the PyStudio Plugin.


---


## Version 0.4 ##

### PyDebug ###
  * Debugger output window should also probably use the Primary Editor font setting for its output

### PyBreakPoint ###
  * Try to find some better icons to use for the Add/Del/Delete all
  * Make column headers sortable (at least for the 'file' column)

### Code Analysis (PyLint) ###
  * Make ListCtrl columns sortable in the [PyLint](PyAnalysis.md) output window. (**Done** version 0.5)
  * Store references to marker objects and use their Handle property to get the current line number instead of line numbers when possible in code analysis tool, since line numbers can change while editing the file. Note: similar functionality will likely also be needed by the debugger.

### PyFind ###
  * Make column header sortable
  * Test and handle additional import statement formats more accurately.

### PyProject ###
  * Add project management support
  * Refactoring support eg. rename all occurrances of a variable/class/method name in all project files
  * Ctrl click to go to function


---
