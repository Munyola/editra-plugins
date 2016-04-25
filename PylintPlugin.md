**NOTE** This plugin has been deprecated in favor of the more enhanced version included in the new PyStudio plugin.

# Introduction #

The purpose of this plugin is to enable the syntax of Python source code to be checked. It can be configured to perform checking automatically on file open/save and change tab or manually by clicking a button. Messages such as Warnings and Errors can be turned on or off in the graphical configuration. Alternatively, there is an optional configuration file in which new paths can be appended to the PYTHONPATH and in which the path to a Pylint configuration file can be specified.

# Detail #

## Graphical Configuration ##

This is available from the Editra Plugin Manager by clicking on Configure for the Pylint plugin.

The plugin will fall back to looking on the system path for the Python executable if the Python Executable Path parameter detailed below is not configured.

If the syntax checker seems not to work or if you wish to change between multiple Python versions, then please specify the Python Executable Path in the graphical configuration.

  * The Python Executable Path is the path to the external Python executable. It defaults to any Python executable found on the system path or will be blank if no Python can be found, in which case the location can be manually specified. This should be the full path to the Python executable file not the folder in which it can be found.
  * The Run Mode is Manual for user activated syntax checking only or Automatic for checking on file open/save and change tab.
  * Messages from the following categories can be individually turned on or off: Convention, Refactor, Warning, Error, Fatal


## Configuration File ##

The configuration file (sometimes called a directory variables file) must be named: `__dirvar_py__.cfg`

When the syntax checker is activated, it looks for this file automatically (without user intervention) in the Python script's current directory, its parent, its parent's parent and so on up the directory tree. Hence, dirvar\_py.cfg could, for example, be put in a project's src folder so that the settings apply to all scripts in src and its subfolders.

Currently, 2 parameters are supported in `__dirvar_py__.cfg`:

  * PYTHONPATH, a comma separated list of paths to add to the PYTHONPATH for Pylint to use
  * PYLINTRC, the path to a Pylint configuration file. This takes precedence over messages settings in the Graphical Configuration.

Relative paths are allowed, for example: . or ..

An example `__dirvar_py__.cfg` might be:
```
PYTHONPATH=../test4,.
PYLINTRC=./pylintcfg/pylintrc
```