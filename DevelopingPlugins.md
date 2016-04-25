# Introduction #

This document is meant to serve as a source of information on setting up a development environment for working on a plugin for Editra.


# Setup #

**1)** Install all required software.
  * Python 2.4+ (2.5 suggested).
  * wxPython 2.8.3+ (latest release suggested)
  * setuptools

**2)** Checkout Editra from svn

`svn checkout http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/Editra Editra `

**3)** Checkout EditraPlugins from svn. Check the folder out under Editra/plugins/ in the folder you checked out above.

`svn checkout http://editra-plugins.googlecode.com/svn/trunk/ editra-plugins`

**4)** Put Editra/plugins into PYTHONPATH environmental variable.

OSX/Linux:
`export PYTHONPATH="$PYTHONPATH:/path/to/Editra/plugins"`

Windows:
{{{Control Panel => System => Advanced => Environmental Variables
Then add it to the system variables.
C:\\Path\to\Editra\plugins.}}}

# How to develop a plugin #

Editra uses python eggs for distributing plugins. A python egg is really just a special zip file with some python files in it. These details are not needed to be known while writing a plugin for Editra but this section will explain some of the options when bundling an egg to make your development time more productive.

1) Typically for Editra to load the plugin your developing you would need to bundle it into an egg each time before running. This can as you imagine get rather tedious. But luckily setuptools has builtin functionality for working around this.

To bundle an egg for distribution you would normally run this command. (assuming cwd is Edtira/plugins/myplugin).

`python setup.py bdist_egg --dist-dir=../`

This will bundle your plugin into an egg and put it in Editra's plugin folder so you can then run Editra and it will be able to find your plugin to try and load it. If you are developing a plugin and bundling to an egg you need to repeat this step each time you make a change to your plugin code.

In order to make this more efficient when developing a plugin you can build it in develop mode so that this step only needs to be done once and then all subsequent changes you make to your code will be automatically linked in to the pseudo develop mode egg.

`python setup.py develop --install-dir=../`

This command will create a folder in Editra/plugins that is a link to your source code in Editra/plugins/myplugin, removing the need to rebuild the egg in between each test run.

2) More info coming soon...

# How to develop a plugin with Eclipse #

Because Eclipse cannot check-out multiple resources into one project, here is what I do to set my environment:

**1)** Checkout Editra from svn using Eclipse SVN tools - create a new project called "Editra"

**2)** Create a new folder called Editra-plugins inside your workspace

**3)** Checkout EditraPlugins from svn. You will create a new project. Set it to live inside "Editra-plugins/plugins" (in the folder you created above)

Thus I have this inside my workspace:
```
c:/dev/workspace/
   Editra/  # Eclipse project
   Editra-plugins/ # folder
      plugins/ # Eclipse project
```

If you have this, you can debug/develop inside Eclipse starting Editra. Open Run/Debug dialog:

  * On the Main tab
    * set project "Editra"
    * Main Module is: ${workspace\_loc:Editra/Editra.pyw}
  * On the "arguments" tab
    * insert into Program Arguments: ` --confdir c:/dev/workspace/editra-plugins `

This will tell Editra to use c:/dev/workspace/editra-plugins as a homedir. Editra will  load plugins' eggs from the plugins directory automatically. (Note, that some folders with configuration data are created in the folder as well)