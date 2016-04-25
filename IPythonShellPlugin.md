# Screenshot #

![http://editra-plugins.googlecode.com/svn/wiki/images/IPythonShellPlugin/Ipyshell.png](http://editra-plugins.googlecode.com/svn/wiki/images/IPythonShellPlugin/Ipyshell.png)

# Introduction #

This plugin creates an interactive python shell that supports autocompletion, good introspection, unix/dos shell commands, %magic keys

**Status**
  * Works under windows,linux and macosx too(thx cody)
  * Alt+c can be used to break infinite loop
  * %cpaste disabled because it supports direct multiline copy/paste on right click
  * Options auto save/load to keep previous startup state
  * Option to select between ipython autocompletion display or scintilla one.
  * Option to select background color
  * History widget : a widget that can be edited and that display all commands previously executed.

**Installation:**
  * New: in version > 0.2 ipython and pyreadline source tree are included in the plugin.
> Just do setup.py bdist\_egg and copy the .egg in plugins directory.

# Implemented IPython Features #

  * ?         -> Introduction and overview of IPython's features.
  * %quickref -> Quick reference.
> > magic keys support: %bookmark
  * help      -> Python's own help system.
  * object?   -> Details about 'object'. ?object also works, ?? prints more.
> > ex: import smtplib then smtplib?
  * !command  -> Execute command in shell ex: !ls,!dir,!cd
  * TAB       -> Autocompletion

# Planned Features #

  * 1)History reload on startup
  * 2)Live help widget : a widget that display help content each time you push a key :) <- hot feature!
  * 3)Script toolbar : a toolbar where button are added from ipython shell to execute scripts :) <- cool feature!

# Known Bugs #
  * Version 0.3:
    * Breaking infinite loop with Alt+c while displaying text can freeze the widget.(Hard to solve)
    * import wx: as this widget use wx app loop, trying to live execute some wx code can result in unexpected behavior.(will be solved in future ipython1 port). Under windows it behave strangely while under linux it seems to work.