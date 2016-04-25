# Introduction #

Commentbrowser allows to see all TODO/FIXME/XXX/HACK statements of the current file or for all currently opened files. It also allows easy navigation to the file and line number of the comment.


# Screenshot #

http://editra-plugins.googlecode.com/svn/wiki/images/commentbrowser/cb_screenshot.PNG

# Usage #

A comment has to stand in a comment region (exception: in python it can also stand in a documentation string) to be listed by the comment browser. It only will list one line comments.

There is a natural priority order: FIXME has the highest priority, then follows XXX, HACK, TODO. You can set the priority of a task by the number of '!' (exclamation marks) in the line of a comment (they have to stand on the same line as the 'TODO:').
For example: '# TODO: !!!! bla'  would have priority 5 (1 for TODO + 4 exclamations marks)

If you double click or right click on an entry in the comment browsers list it will navigate to the line of code in the corresponding file.

You can switch between seeing all comments for all currently opened files or just for the current file.

Filtering of the different task types is also provided. Each column can be sorted (it is sorted in an intelligent multicolumn manner).

In most cases it will update automatically, but to be sure there is an 'update' button.