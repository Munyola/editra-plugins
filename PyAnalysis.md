

# Introduction #

This page contains information about how to use and configure the code analysis features provided by the PyStudio plugin for analyzing Python code. This component provides a fully integrated user interface for performing code analysis on Python code.

**NOTE:** If you have previously installed the standalone PylintPlugin it is suggested to uninstall it prior to installing PyStudio as the functionality of that plugin has been deprecated based on the new improved functionality provided by the PyStudio plugin

# Configuration #

Configuration options for the code analysis tools are located in the PyStudio configuration dialog, for [general configuration](PyStudio#General_Configuration.md) information please see the PyStudio page. PyLint specific configuration options are discussed below.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/PyStudio_config_code_analysis.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/PyStudio_config_code_analysis.png)

The code analysis can run in one of two modes, Automatic or Manual. The default setting is Manual which means the analysis is only run when the Analysis button is clicked. Setting the option to Automatic will tell it to run after every time a file is saved.

The PyLint Checkers configuration allows for turning specific issue checkers on and off. This allows you to fine tune the kinds of issues you want to check for in you code. The default configuration is with everything enabled.

# Basic Usage #

This section contains the basic usage information for this component, the screenshot below will be used for reference throughout the next part of this section.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pylint_main.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pylint_main.png)

**Buttons**
  * The first button on the left hand side will bring up the PyStudio Configuration dialog.
  * The second button is for exporting analysis results to an XML file
  * The third button is for loading results from an XML file
  * The Analysis button will run PyLint on the current file open in Editra.
  * The Clear button can be used to clear the result list and the bug markers from the text editor buffer.

The following screenshot shows an example of running the analysis on a file in Editra.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pylint_analyze.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pylint_analyze.png)]

When the analysis is run it will list all of its results in the Shelf window. Double clicking on any item in the list will jump to the corresponding line in the buffer. In addition to this small bug markers are added to the text buffer to quickly show where issues where noted by the analysis. Hovering the mouse over a line that has one of these markers will show a tooltip that contains the details of the findings for that line.

There are three kinds of analysis markers that can be shown in the left most column. The markers are color coded depending upon the severity.

  1. Green Marker - Convention or other low priority issue
  1. Yellow Marker - Warning message
  1. Red Marker - Error message

# Exporting/Importing Results #

If you want to save the results of the analysis to use later or for gathering metrics between runs the PyLint shelf window provides the option to export the results list to an XML file. The resulting XML is formated as shown in the screenshot below.

![http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pylint_export_xml.png](http://editra-plugins.googlecode.com/svn/wiki/images/PyStudio/pylint_export_xml.png)

This file can be imported back in and displayed in the shelf window at a future time as well to continue with resolving issues noted by the analysis.

# Related Pages #
PyStudio