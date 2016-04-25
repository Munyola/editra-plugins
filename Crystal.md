# Introduction #

This plugin is a theme plugin that can be installed through Editra's plugin manager to provide the Crystal Project Icons for Editra's toolbar, menus, dialogs, ect..

This icon uses the new theme interface that is available in versions of Editra > 0.2.0.


# Details #

This icon theme plugin is distributed under the LGPL for more information about the Crystal Project icons see http://www.everaldo.com/crystal/?action=downloads

# Preview #

![http://editra.org/images/plugins/Macintosh/crystal.png](http://editra.org/images/plugins/Macintosh/crystal.png)

# Installation #

1) Automatic Install: Open the PluginManager (Tools=>PluginManager), then choose download to download and install this theme.
2) Manual Install: Download the _egg_ file and drag and drop it on to the Installation page of PluginManager.

After the theme is installed in can be set for use by going to Preferences=>Appearance=>Icon Theme and choosing Crystal.

# Build Guide #

To build the plugin into an egg from source do the following:

  1. cd crystal
  1. python setup.py bdist\_egg

This will build and put the egg in a directory called _dist_ that is the same directory as the setup.py file.