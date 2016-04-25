

# Introduction #

Provides a collection of tools to aid in the development of Python applications.


---


# Main Features #

  * PyProject (Project Management **new version 0.7**)
  * PyDebugger (Integrated Remote Python Debugger via [Winpdb](http://winpdb.org/) backend)
  * PyFind (Python Module Finder)
  * [Code Analysis](PyAnalysis.md) (Integrated Code Analysis via [PyLint](http://www.logilab.org/857))

# Minor Features #

  * [Right click Open Module](PyStudio#Open_Module.md)
  * [Syntax Error Check](PyStudio#Syntax_Error_Check.md)


---


# Installation Notes #

**NOTE:** If you have previously installed the standalone PylintPlugin it is suggested to uninstall it prior to installing PyStudio as the functionality of that plugin has been deprecated based on the new improved functionality provided by the PyStudio plugin


---


# Details #

PyStudio is a collection of tools for working with and developing Python code. This page contains the general information about the plugin, please see the links to the various features of the plugin for more detailed information.


---


# General Configuration #

The PyStudio configuration dialog can be accessed from any of the plugins Shelf windows as well as from the PluginManager dialog. The screenshot below shows the General configuration page.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/PyStudio_config_general.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/PyStudio_config_general.png)

The PyStudio plugin tries to automatically detect what Python your using on your system but to get started you should make sure that this path is pointing to the Python that you want to work with. Most features of this plugin rely on this setting when running Python related commands.

## Configuration File ##

It is possible to specify an optional configuration file (sometimes called a directory variables file). It must be named: `__dirvar_py__.cfg`

When the tools are activated, they look for this file automatically (without user intervention) in the Python script's current directory, its parent, its parent's parent and so on up the directory tree. Hence, `__dirvar_py__.cfg` could, for example, be put in a project's src folder so that the settings apply to all scripts in src and its subfolders.

Currently, 3 parameters are supported in `__dirvar_py__.cfg`:

  * PYTHONPATH, a comma separated list of paths to add to the PYTHONPATH for tools to use
  * PYLINTRC, the path to a Pylint configuration file. This takes precedence over messages settings in the PyStudio configuration dialog.
  * DEBUGGERARGS, arguments to the debugger. The PyStudio configuration dialog setting "Debugger Args" takes precedence over this setting. %SCRIPT% can be used to refer to the current Python script or %MODULE% if it is required in module form (ie. xxx.yyy.zzz).

Relative paths are allowed, for example: . or ..

An example `__dirvar_py__.cfg` might be:
```
PYTHONPATH=./src,./test
PYLINTRC=../.pylintrc
DEBUGGERARGS=./src/run.py %MODULE%
```


---


# Open Module #

The Open Module feature allows you to right click on an import statement and open the corresponding module. When an import statement is clicked on the buffers context menu will include the "Open Module" menu item as shown in the below screenshot.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/open_module_ctx_menu.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/open_module_ctx_menu.png)


---


# Syntax Error Check #

The syntax error check option (defaults to on) will automatically check files for syntax errors and other typos when the file is saved.

The screenshot below shows the syntax error checker marking an error it found in the file.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/syntax_error_checker.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/syntax_error_checker.png)

Hovering over the line with the error will show a tooltip providing more details about the error.


---


# TODO List #

[TODO List for Future Releases](PyStudioFuture.md)