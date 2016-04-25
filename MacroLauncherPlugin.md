# Introduction #

![http://editra-plugins.googlecode.com/svn/wiki/images/MacroLauncher/mlauncher_example.png](http://editra-plugins.googlecode.com/svn/wiki/images/MacroLauncher/mlauncher_example.png)

_Above is the screenshot of the Editra with MacroLauncher enabled - the two green lines are two macros currently running (you can see their output in the log window), and I am about to start the third macro._



Macro Launcher (MLauncher) helps you to write and **execute** short (or long) python
scripts. The scripts can do variety of tasks, basically, in Editra you will have a nice graphical interface for controlling them.

Here are some ideas where MacroLauncher helps me:

  * automate tasks inside Editra (e.g. sorting files, removing spaces)
  * help developing plugins (I am using it to reload plugins without restarting Editra)
  * change Editra settings, GUI etc.
  * run testunits for Editra development (ie. test if something works inside wx App)
  * script external programs, fire up long-running tasks in threads in the background
  * use Editra as portable Python (put Editra on the usb key, use MacroLauncher to write/execute scripts)

As a short note: I am calling the scripts inside MLauncher "macros" but
they are just normal python code (that you have to write or download)

Basic features of the plugin:

  * Create new macro / Edit existing macro directly in Editra
  * Control macro execution (Start/Stop)
  * Filter macros by type
  * Automatic reloads on edits / Forced reload (user requested)
  * Quick view of the macros
  * Protect macros against changes

## Installation ##

Use Editra Plugin Manager to download the plugin. (Go to the Plugin Manager under the Tools menu. Simply enable it, restart Editra, and then choose MacroLauncher from the View menu.)


The source can be obtained from the following Subversion repository:

> svn checkout http://editra-plugins.googlecode.com/svn/trunk/MacroLauncher

The plugin will install a few example macros for you at a startup so you can start playing with it. (Try clicking on the documentation# macro, that one will show this help in the Editra)

## Configuration ##

There isn't much you can do - MacroLauncher helps you to execute macros, therefore most of the time you spend by writing them. Macros will be placed in your Editra profile folder (eg. ~/Editra/macros)

## Usage ##

Very simple: download or create macro - execute - wait/work on something else


### New Macro ###
```
 1. Click on New Macro button (new editor with a basic template will open)
 2. Write your code
   * when you hit Ctrl+Save, the code of the plugin is automatically
     reloaded
 3. Run the macro
   * by double-clicking its entry in the panel
   * by selecting and clicking on the icon "Run"
   * by selecting and pressing Enter 
```

Here is the example of a basic macro:

```

# -*- coding: utf-8 -*-

__name__ = 'sort-example'
__type__ = 'example'
__desc__ = 'Sort lines by Czech locale'

import locale
locale.setlocale(locale.LC_ALL,"cz")

def run(txtctrl = None, **kwargs):
  if txtctrl:
    lines = txtctrl.GetText().splitlines()
    lines.sort(cmp=locale.strcoll)
    txtctrl.SetText(txtctrl.GetEOLChar().join(lines))

```

This macro will take the text from the current buffer, split it into lines, sort it alphabetically (using cz locale) and replace the contents of the current buffer with the results.

Few things to note:

  * name is the name of the macro as shown in the left-most column in the panel
  * type is the way to group macros (you can filter macros by type)
  * desc is a description, is displayed in the right most column
  * when you execute macro, the run() function is called
  * whenever you edit macro in Editra, the macro is reloaded after save

If there is a syntax error, macro will be highlighted with red line. The error message will be shown in the Editra log (so activate the Editra log window, if you want to see something).

The macro has a separate namespace, basically you cannot change the Editra environment by, for instance, loading its modules and manipulating some classes.  This will not work:

```
from Editra.src.profiler import TheProfile #TheProfile is singleton
TheProfile.DeleteItem('something') # will not work with Editra's current profile
```

What you share with Editra is just builtins and the passed in instances. So if you want to do some funcy stuff, either you have to get reference for the instance from the passed in arguments available to your macro, or you have to do hacks like this

```
import sys
module = sys.modules['src.profiler'] #you have to find out the name of the module yourself
profile = module.TheProfile
profile.DeleteItem('something')
```

Keyword arguments available to your macros are these:
  * txtctrl: wx.stc current editor
  * nbook: notebook instance
  * win: the main window
  * log: log method for writing into the Editra log
  * mlauncher: macro launcher instance (plugin itself)


### Macro types ###

There are two types of macros:
  1. blocking macro (started by call run())
  1. threaded macro (started by call to run\_thread())

Threaded calls are started in a new thread (yes, you guessed it) which
means that editor remains responsive even if the macro is running -
and it can do some very complicated calculations, database queries etc.

If you use run\_thread() for tasks that interact with Editra, a lot of
caution is needed. Because some operations are allowed only from the main
thread. For instances if you do this, Editra will crash (and you won't
even have time to blink):
```
    def run_thread(nbook = None, **kwargs):
      nbook.AddPage()
```

This will be fine (call from the main thread):

```
    import wx
    def run_thread(nbook = None, **kwargs):
      wx.CallAfter(nbook.AddPage)
```

For the best performance, the function run\_thread() should periodically
return by yield():

```
    import time
    def run_thread(**kwargs):
        for x in range(5):
            time.sleep(.5)
            yield x
```

Look at the supplied macros for examples. Try to select all macros
of type 'thread', right-click and choose run. You can start threaded
and non-threaded macros together. If the threaded macros are first on
the list, you will not wait.




## Additional info ##

Where are the macros saved?
> They are saved inside the .Editra configuration directory (.Editra/macros)
> Where you can edit them, delete, copy etc. (But use the plugin interface
> for that)

To protect macro:
> Insert '#' in the name. Editor will refuse to delete/edit such a macro.

Example macros:
> Together with the plugin, you will find some example macros. This help is
> one of them. They are installed automatically (and may be overwritten by
> new versions, so do not save your work in them!)

Macro filenames
> The automatically created macro have special filename, but it is not important
> to follow any conventions. Except for one. The macros that have in its name
> '_overwrite.' may get overwritten by future updates._


## About - credits ##

  * The idea of the Macro Launcher comes from the Pype editor.
  * Parts of the code from the commentbrowser by DR0ID (dr0iddr0id at googlemail com)
  * Of course, MLauncher is using Editra codebase and Cody Precord helped fixing a few issues
  * The little what is left is by me, rca (http://www.roman-chyla.net)


## TODO ##

  1. repository of downloadable macros?
  1. select macros and run the all in one-after-another mode (chained)
