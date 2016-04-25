# Introduction #

There are two major groupings of settings: general settings for the behavior of the Projects plugin and settings for source control commands.  Then, of course, there are the projects themselves.  These major areas are discussed below.

# Adding and Removing Projects #

Creating a new project is as simple as clicking on the leftmost button (see figure below) in the Projects panel and selecting a directory.

![http://editra-plugins.googlecode.com/svn/wiki/images/Projects/toolbar.png](http://editra-plugins.googlecode.com/svn/wiki/images/Projects/toolbar.png)

Once a directory has been added, the Projects plugin automatically tracks the visible directories and files.  If files are added or deleted in the file system, the tree view in Projects will reflect those changes.  In addition to that, the Projects plugin also tracks all source control attributes.  The icon for the file will show the current status of the file.  If you do not see the icons reflecting the status of files under source control, see the Source Control Settings section below.

Removing a project is even easier than adding one.  Simply select the project you want to remove and click the center button on the toolbar.

# General Settings #

The General settings in Projects modify the overall behavior of the plugin.  There are just a few things that can be set in here: file filters, notebook synchronization, and the program used for file comparisons.

![http://editra-plugins.googlecode.com/svn/wiki/images/Projects/general.png](http://editra-plugins.googlecode.com/svn/wiki/images/Projects/general.png)

## File Filters ##

The file filters area simply takes a space-separated string of file patterns that you **do not** want to display in the tree view.  This may include backup files, source control setting directories, compiled object files, etc.  Pretty much anything that you aren't going to be editing in Editra is a good candidate for putting in here.

The file filters string uses wildcards just like in UNIX shells.  These patterns can be interspersed with strings of characters to create patterns like `*.log` for all files with a '.log' extension, or `file?.txt` for files that start with 'file' then any single charater followed by a '.txt' extension.  The patterns shown in the table below can be used any number of times within a filename specification.

| **Pattern** | **Meaning** |
|:------------|:------------|
| `*`         | Matches any number of characters |
| ?           | Matches a single character |
| `[`_seq_`]` | Matches any character in the sequence (e.g., `[`A-Z`]` or `[`0-9`]`) |
| `[`!_seq_`]` | Matches any character not in the sequence (e.g., `[`!X-Z`]` or `[`!0-3`]`) |

## Notebook Synchronization ##

By default, if a file that is opened in the Editra notebook exists in one of your projects, that project tree is expanded to display the file.  This behavior can be turned off so that folders will only expand when clicked manually.

## File Comparisons ##

When doing file comparisons of files under source control, you can either use the built-in diffing utility which simply generates an HTML file showing the diffs and opens your default web browser with that file, or you can specify your own utility.  This utility should simply accept two command line arguments for the two files to compare.

# Source Control Settings #

Each source control system has a setting for the command to run when invoking source control operations and settings for each repository that belongs to that system.  The command is fairly simple.  It is just the path to the command itself.  Settings for the repository are more extensive and are described in the following section.

![http://editra-plugins.googlecode.com/svn/wiki/images/Projects/source-control.png](http://editra-plugins.googlecode.com/svn/wiki/images/Projects/source-control.png)

## Repository Settings ##

If all of your repositories for a given source control system use the same settings, you can simply put your authentication and environment variable settings in the Default repository.  Settings in the Default repository are applied regardless of which repository is actually being used.  Of course, you can override the Default settings by adding a new repository using the **Add Repository...** selection in the drop-down list.  The name for the repository should match the repository path that you want the settings to be used for.  In the case of CVS, this might be something like `:ext:myid@x.net:/cvsroot`.  Once created, you can set values for authentication and environment variables that will be applied when doing source control operations on files and directories in that repository.

Not only can you specify the full repository path, you can also specify partial paths.  Any repository path that is a prefix of the repository being operated on will also be matched. For example, let's say that you have two projects with slightly different configurations at `:ext:myid@x.net:/cvsroot/abc` and `:ext:myid@x.net:/cvsroot/xyz`.  You can put the common settings for these repositories under `:ext:myid@x.net:/cvsroot` and only put the settings specific to the 'abc' and 'xyz' projects into the `:ext:myid@x.net:/cvsroot/abc` and `:ext:myid@x.net:/cvsroot/xyz` repository configurations, respectively.  Longer repository path match settings have a higher precedence than short matches.  The Default settings have the lowest priority.

## Authentication ##

It should be noted at this time that not all source control systems support authentication on the command line.  In fact, the only one that supports it at this time is Subversion.  This means that setting authentication information in other source control systems will do nothing.  This will probably change in future versions of the plugin, but you should be aware that for any source control systems other than Subversion, if you can not do source control operations without entering your name or password interactively, this plugin will not work.
