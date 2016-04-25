# Introduction #

This page is meant to give a brief overview on how to make a new plugin able to use translations. This guide assumes that the whole project has been checked out of svn.

# Setup #

In creating a plugin be sure to do the following in any modules that provide UI components.

```
import wx
_ = wx.GetTranslation
```

Then wrap any Ui strings that should be translatable with `_()` (i.e `_("Hello")` )

In the base of this projects checkout directory there is a script called **gen\_lang** that can be used to generate and setup all the localization resources for a plugin. To use it simply run the following command from the base of the projects directory, replacing PLUGIN\_NAME with the name of the directory for the plugin you wish to generate/synchronize localization resources for. It will syncronize/merge existing translations and generate/create any non-existent/new resources.

```
./gen_lang -p PLUGIN_NAME
```

This will create all the po files and put them in PLUGIN\_NAME/catalogs. The next step is to compile them into machine object file by running.

```
./gen_lang -m PLUGIN_NAME
```

This will create all the mo files and put them in PLUGIN\_NAME/PLUGIN\_NAME/locale

# Code #

The following code should be put in the plugins `__init__.py` module. The only part that needs to be changed is to replace MOFILE\_NAME with the name of the generated locale file found under `locale/xx_XX/LC_MESSAGES/xxxx.mo` without the mo extension. The name of the mo file should be the same as that of the given plugins top level directory in the project. So for example the Projects plugin would use the following code since its mo files are called "Projects.mo".

```
# Try and add this plugins message catalogs to the app
try:
    wx.GetApp().AddMessageCatalog('Projects', __name__)
except:
    pass
```