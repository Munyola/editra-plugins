# Introduction #

This plugin project has two parts:

This plugin creates a terminal widget that emulates the system shell such as /bin/bash or cmd.exe on Windows.

## Status ##

Currently it works well on Unix like systems (Macintosh OSX, Linux). There are still some outstanding issues with running it as a plugin inside of Editra however so currently it is suggested to only use it as a standalone program by running terminal.py.

There is also code in place to get it running on Windows that is mostly untested. Windows doesn't have support for pty's though so it requires its own set of commands using pipes instead.

# Implemented Features #
  * Basic framework is in place and it can be used just like your system shell but still has a number of display and behavior issues to fix up before an official release.
  * Support for ANSI color code escape sequences to allow for coloring of different file types.
  * Command history recall with Up and Down keys.

# Planned Features #

  * Key interupts
  * Customizable appearance, font, colors, ect...
  * Configurable line buffering for ui display
  * Search output by linking into Editra's quick find bar