# Introduction #

The Css optimizer plugin is an Editra Generator that generates css files that are optimized for size. It works by taking the css file that is in the current buffer and removing comments and compressing extra whitespace. In order to preserve some level of readability though definitions are only compressed to one definition per line.

  * Removes Comments
  * Compacts extra whitespace
  * Compacts color values into smaller strings

# How To #

This plugin will only work with if the file in the current buffer is recognized as css. This means that either the css lexer is set or the file has a file extension that matches the patter set in the lexer preferences for css files.

When a css file/text is in the current buffer simply go to _Tools_=>_Generator_=>_Optimize CSS_. The generator will then optimize the text in the current buffer and place the new text in a new buffer as to not overwrite the original file.