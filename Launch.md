# Introduction #

Launch is a plugin for running a program on the contents of the current buffer and being able to view the output in the Shelf. If the current buffer contains a script it can be used to run and test the script, or if configured as such it can be used to run lint programs such as pylint on the current buffer.

**Note** This plugin is not hosted by this project but is included in Editra core (>0.2.50). See the project homepage for more details (http://editra.org)


# Features #

  * Save and configure multiple executables per file type
  * Custom output styling and handling depending on file type
  * Hotspots in errors allow for automatic navigation to the error in the affected file
  * Automatic notebook synchronization
  * Abort running processes at any time
  * Support for multiple instances at one time open in the Shelf

# Supported File Types #

  * Bash Shell
  * Boo
  * C-Shell
  * Ferite
  * haXe
  * Korn Shell
  * Lua
  * NSIS
  * Perl
  * Php
  * Pike
  * Python
  * Ruby
  * Tcl/Tk

# Installation #

This plugin is bundled and installed by default with all binary versions of Editra >= 0.2.65. To use it simply enable it in the PluginManager (Tools=>PluginManager)

If you are using a source version of Editra the plugin can also be installed via the PluginManagers builtin downloader. Simply open the PluginManager and choose it from the download list, if it is not listed in the list it means it is already installed.

# Usage #

Quick list of key points more details after its first release

  * Open an instance (View=>Shelf=>Launch)
  * Click on _Run_ to run the selected program on the current buffer
  * To stop the process click on _Abort_ at any time
  * The output can be cleared with the _Clear_ button
  * Configuration can be done by clicking on the settings button found on the top left of the window