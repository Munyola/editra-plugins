

# Introduction #

This page contains detailed information about the PyDebugger component of the PyStudio plugin. PyDebugger is a debugger based off of the same rpdb2 Python debugger that is used by Winpdb. This component contains a collection of various shelf windows and editor integration for debugging Python programs and scripts. See the sections below for an introduction to each part of the debugger.


---


# Configuration #

This section contains information specific to the configuration of the debugger, for [general configuration](PyStudio#General_Configuration.md) see the main PyStudio page.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/PyStudio_config_debugger.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/PyStudio_config_debugger.png)

**Options**
  * Trap Unhandled Exceptions
  * Enable Synchrocity
  * Pause Before Fork
  * Fork into Child
  * Source Encoding
  * Escape non ascii characters for Execute/Evaluate

## Trap Unhandled Exceptions ##

If enabled, debuggee will pause on unhandled exceptions for inspection, otherwise it will ignore them.

## Enable Synchronicity ##

Traditional Python debuggers that use the inspected thread (usually the main thread) to query or modify the script name-space have to wait until the script hits a break-point. Synchronicity allows the debugger to query and modify the script name-space even if its threads are still running or blocked in C library code by using special worker threads. In some rare cases querying or modifying data in synchronicity can crash the script. For example in some Linux builds of wxPython querying the state of wx objects from a thread other than the GUI thread can crash the script. If this happens or if you want to restrict these operations to the inspected thread, turn synchronicity off. On the other hand when synchronicity is off it is possible to accidentally deadlock or block indefinitely the script threads by querying or modifying particular data structures.

## Pause Before Fork ##

If enabled, debugger will pause before doing a fork, otherwise it will automatically fork into the parent or child process depending upon the option Fork into Child.

## Fork into Child ##

If enabled, the debugger will switch to debug the forked
child process after a fork, otherwise it will continue to debug the original parent process after a fork.

## Source Encoding ##

Set the encoding of the files being debugged.


---


# PyDebugger Components #

## PyDebug ##

The PyDebug Shelf window is the main control window for attaching to programs and stepping through the code. The screenshot below shows what the debug window looks like.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_debugger.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_debugger.png)

**Actions** (from left to right)
  * Preferences Button - Open the PyStudio configuration dialog
  * Go Button - Start debugging the current script or tell the program that is already being debugged to run to the next breakpoint.
  * Stop Button - Abort the debug session
  * Step In Button - Step into the call on the current line
  * Step Over Button - Step over the current line
  * Step Out Button - Step out of the current scope
  * Break All Button - Break at the current point of execution
  * Program/Debugger Args Choice Control
  * Text Field - enter arguments to pass to the program or debugger based on selection in previous field.
  * Remote Button - Attach to an already running process


---


## PyBreakPoint ##
The PyBreakPoint Shelf window is for displaying and managing breakpoints. The screenshot below shows the PyBreakPoint window and how the breakpoints are displayed in the editor.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_breakpoint.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_breakpoint.png)

Breakpoints can be added to any line of code in the editor. There are three ways to add a breakpoint to a line.
  1. Click in the marker margin on the far left of the editor window. Clicking again will toggle the breakpoint off.
  1. Right clicking on the line and selecting the Toggle Breakpoint option to toggle a breakpoint on the line.
  1. Clicking the + button that is displayed on the breakpoint window's control bar will add a breakpoint to the line in the text buffer that the cursor is currently active on.

**Actions**
  * Preferences Button - Open the PyStudio configuration dialog
  * Add breakpoint - Click the + button that is displayed on the breakpoint window's control bar will add a breakpoint to the line in the text buffer that the cursor is currently active on
  * Delete breakpoint - Click the - button to delete the currently selected breakpoint
  * Delete all breakpoints - Click the button right of the - one to delete all breakpoints in the list
  * Enable/disable breakpoint - Click on the red breakpoint marker that is shown in the list to disable or re-enable a breakpoint
  * Conditional breakpoint - A conditional breakpoint can be made by creating a normal breakpoint as above and then clicking on the Expression column for the appropriate breakpoint in the Shelf Window. The expression text can then be entered
  * Jump to breakpoint line - Double clicking on a breakpoint will cause the cursor to jump to that point in the code


---


## PyExpression ##

The PyExpression Shelf window is for managing expressions and displaying their evaluated results. The screenshot below shows the PyExpression window.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_expression.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_expression.png)

Expressions are evaluated while the program is being debugged when it is stopped at a breakpoint.

**Actions**
  * Preferences Button - Open the PyStudio configuration dialog
  * Add expression - Click the + button that is displayed on the expression window's control bar to add an empty expression
  * Change expression - Click on the column and type the desired expression to enter an expression
  * Delete expression - Click the - button to delete the currently selected expression
  * Delete all expressions - Click the button right of the - one to delete all expressions in the list
  * Enabled/disable expression - Click the checkbox next to an expression to enable or disable its evaluation
  * Refresh expressions - Click button to force a reevaluation of expressions
  * Execute user code - Press the Execute button to execute some Python code (when stopped at a breakpoint)


---


## PyStackThread ##

The PyStackThread Shelf window provides a view of the current execution stack and thread statuses of the program being debugged. The screenshot below shows this window in the Stack view.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_stack.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_stack.png)

**Views**

Using the vertical control bar on the left this window can display one of two views.

  * Stack - Shows the current execution stack
  * Threads - Shows the status of the running threads

**Actions**
  * Preferences Button - Open the PyStudio configuration dialog
  * Move up/down stack - Double clicking on an item in the stack list will jump to that point in the code
  * Move between threads - Double clicking on an item in the thread list jumps to that thread


---


## PyVariable ##

The PyVariable Shelf window provides a way to inspect the local and global variables that are present in the current debug context. In addition to this it also allows you to inspect any exceptions that may have been thrown by the debuggee.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_variables.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pydebug_variables.png)

**Views**

The control bar on the left contains buttons to activate one of the three possible views. Hovering over the button will show a tooltip describing the view but from top to bottom the views are.

  * locals()
  * globals()
  * Exceptions

**Actions**
  * Preferences - Open the PyStudio configuration dialog
  * Filter - Show only data that matches a regular expression and/or set the verbosity of how much data is shown in each view
  * Analyze Exception - Set the program state back to when the exception was raised and left uncaught
  * Change variable - Double clicking on a variable allows its value to be changed
  * Add variable - Right clicking on a variable adds it to the PyExpression shelf
  * Refresh variables - Click button to force a reevaluation of variable values