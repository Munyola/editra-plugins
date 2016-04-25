# Introduction #

**Unmaintained and mostly superseeded by the new Launch plugin**

PyRun is a Shelf plugin that can run the script that is in the current buffer and display its output in a text buffer in the Shelf. The scripts can be launched using the hotkey that PyRun is assigned by the shelf (Cmd+Alt+_Number Key_), after a PyRun instance is open in the Shelf the script can be rerun by using the "Run Script" button.


# Current Features #

  * All output from running script shown in a builtin output buffer in Editra's Shelf.
  * Run multiple scripts simultaneously without blocking usage of any other parts of Editra
  * Abort a running script at any time
  * Configure which python executable to use for running script(s)
  * Synchronizes with the currently selected buffer in Editra
  * Colorize error messages in Red
  * Clicking on an Error message in the output buffer will go directly to the line of the error in the file it occurred in


# Planned Features #

  * Save and configuration for multiple versions of python and allow easy switching at runtime


# Installation #

> Soon to be officially released and available to Editra's builtin plugin downloader, to check out an prerelease copy of it do the following.

  * Check out from svn
> `svn checkout http://editra-plugins.googlecode.com/svn/trunk/PyRun PyRun`

  * Build the plugin
> `python setup.py bdist_egg`

  * Open Editra=>Tools=>PluginManager=>Install, then Drag and Drop the egg file on the window and click 'Install'


# Usage and Configuration #

This plugin requires little to no configuration for usage. Simply open an instance of it from **View=>Shelf=>PyRun** and it will open and automatically run the script thats in the current buffer. If it fails to run, Python might not be on the PATH. In this case simply enter the path to the desired Python executable into the text entry labeled "Python Executable" to tell PyRun which python to use.

When an instance of PyRun is open in the Shelf it will automatically sync with what buffer is the currently selected one in Editra's main notebook. The script can then be run by clicking on the "Run Script" button.