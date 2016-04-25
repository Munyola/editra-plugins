# Introduction #

CodeTemplater is an Editra plugin for adding commonly-used templates to your code quickly and efficiently.  This makes consistent use of common design patterns and pythonic idioms much simpler.

CodeTemplater is compatible with Editra v0.5.15 or later


# Using Templates #

Code Templates are added by choosing the Tools > Code Templates > Show Code Templates, or the appropriately bound key (default Ctrl+Alt+space).  This triggers the pop-up for the appropriate language and allows a code template to be selected with arrows keys for insertion at the location of the current cursor when the user hits enter (deleting any text that is selected).  Esc will cancel the pop-up.


![http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/niebefore.png](http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/niebefore.png)

![http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/nieafter.png](http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/nieafter.png)


Some Templates also use the currently selected text for content.  In the below example, the 'property' template uses the currently selected text as the name of the property it creates, as well as for the getter and setter method names.

![http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/sillybefore.png](http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/sillybefore.png)

![http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/sillyafter.png](http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/sillyafter.png)

# Editing Templates #

To change or add new templates, open the dialog at Tools > Code Templates > Edit Templates.

![http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/editdiag.png](http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/editdiag.png)

There are separate sets of templates for every language that Editra supports, which can be selected with the drop-down menu on the upper-left.  This also sets which language is active in the main Editra window, although it may be changed when switching windows.

To Edit an existing template, simply select it from the list on the left, and change text fields on the right side of the panel. The name is used in the pop-up menu and hence should be short, while the help text should be more descriptive (it is the tooltip associated with the item).  The "Obey Indentation" option determines whether or not all the lines will by indented to whatever the current indentation is when the template is added.

The actual content of the template can be changed in the large text box.  The template will be added as shown here, indented to the current indentation if "Obey Indentation" is checked, but with certain special character combinations replaced based on the selected text.  These special codes are summarized in the box:

  * ${same} : replaced with the selected text exactly as-is
  * ${upper} : replaced with the selected text with the first character set to upper case
  * ${lower} : replaced with the selected text with the first character set to lower case
  * $$ : an actual "$" character
  * #CUR : this code will be deleted when the template is added and the cursor will be set to this location

Finally, the buttons on the bottom can be used to close the window, save the templates to your profile (if you don't do this, all changes will be lost as soon as you exit Editra), or reset all profiles to the default values.


# Configuration Options #

The configuration panel has two options:
  * The command key used to trigger the "Show Code Templates" action.
  * A "Synchronize language with file type?" checkbox indicating if the language used for the code templates should be changed to match whatever file is selected.  The Edit Templates dialog sets the language if this is not checked.

![http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/cfgdlg.png](http://editra-plugins.googlecode.com/svn/wiki/images/CodeTemplater/cfgdlg.png)

# Submitting Default Templates #
Currently, the only templates in the default collection are for Python.  Users are encouraged to submit templates for other languages either on this wiki or via e-mail to the author of this plugin, and they will be included in the default collection at a later date.