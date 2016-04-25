# Introduction #

The Projects plugin integrates the features of a file manager and source control into a self-contained, easy to use side panel.  Simplicity and transparency is the main focus of the Projects plugin.  It requires no "project files" and almost no configuration.  The Projects plugin treats directories as projects.  You simply add a directory as a project and the Projects plugin automatically tracks files in that directory.  If the files are under source control (currently CVS, Subversion, GIT, Bazaar, and Mercurial are supported), the icons for those files will indicate the status of the files.  You can also do most source control operations using the right-click menu.


# Current Features #

This plugin is still in early development, but is quite useful in its current implementation nonetheless.  Below is a list of the current features.

  * Add/remove project directories
  * Files and directories are automatically synchronized with the file system
  * Copy/Cut/Paste of files and directories
  * Open files and directories in editor
  * Open files using Finder/Explorer
  * Reveal files in Finder/Explorer
  * Delete files and directories
  * Automatically filter out temp and bak files from view
  * Configurable list of file pattern filters
  * Rename by editing tree node text
  * Multiple file/directory selections
  * Progress indicator for long operations
  * Automatically display file from currently selected editor tab in project view (if file exists in a project)
  * Utilize system's Trash / Recycle Bin
  * Seamless source control integration (Bazaar, CVS, GIT, Mercurial, Subversion)
  * Make Patch from diff of selected files and open it in the editor

The following are the currently implemented source control features that are available for each of the supported systems that can be executed on either files or directories.  The status features are automatic.  Other features are accessed using the right-click menu.

  * Automatically displays status of files and directories in icons when folder is opened
  * Refresh status
  * Update files
  * Compare to previous version using FileMerge or other file comparing tool
  * Revert to repository version
  * Commit changes (dialog for message entry)
  * Configurable commands for Bazaar, CVS, Git, Mercurial, and Subversion
  * Add to repository
  * Remove from repository
  * Revision history window with ability to compare playpen version to any previous version, as well being able to compare any two repository versions
  * Configurable environment variables based on file/directory path

# Installation #

Installation is done just as it is for any other Editra plugin.  You can either download the released Python Egg file and install it into your ~/.Editra/plugins/ directory, or install from the source.  The source can be obtained from the following Subversion repository:

```
    svn checkout http://editra-plugins.googlecode.com/svn/trunk/Projects
```

Then you run the following commands to create and install the Egg file (Windows users would use 'move' instead of 'mv'):

```
    python setup.py bdist_egg
    mv dist/*.egg ~/.Editra/plugins/.
```

The Projects plugin should now be available in the Plugin Manager under the Tools menu.  Simply enable it, restart Editra, and then choose Projects from the View menu.

# Configuration #

There aren't that many configuration settings for the Projects plugin.  It is meant to be non-invasive, and to "just do the right thing at the right time."  There are some settings that may be needed to get source control commands to work in Editra.  The source control configuration and other settings are described in ProjectsConfiguration.

# Planned Features #

The following list of features are planned for general file management and editing.

  * Drag-and-drop moves, additions, and deletions
  * File type appropriate icons
  * Interactive filtering of tree (like in wxPython demo app)
  * Run shell commands on files/directories