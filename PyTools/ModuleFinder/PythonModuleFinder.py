# -*- coding: utf-8 -*-
# Name: PythonSyntaxChecker.py
# Purpose: Pylint plugin
# Author: Mike Rans
# Copyright: (c) 2010 Mike Rans
# License: wxWindows License
##############################################################################
""" Pylint module for Python data """

__author__ = "Mike Rans"
__svnid__ = "$Id: PythonModuleFinder.py 1053 2011-02-08 22:09:37Z rans@email.com $"
__revision__ = "$Revision: 1053 $"

#-----------------------------------------------------------------------------#
# Imports
import os
import pkg_resources

# Local Imports
from Common import ToolConfig
from Common.PyToolsUtils import PyToolsUtils
from Common.ProcessRunner import ProcessRunner
from AbstractModuleFinder import AbstractModuleFinder

# Editra Imports
import util
import ebmlib

#-----------------------------------------------------------------------------#

class PythonModuleFinder(AbstractModuleFinder):
    def __init__(self, variabledict, moduletofind):
        super(PythonModuleFinder, self).__init__(variabledict, moduletofind)
        
        # Attributes
        self.dirvarfile = variabledict.get("DIRVARFILE")
        self.pythonpath = variabledict.get("PYTHONPATH")
        self.nopythonerror = u"***  FATAL ERROR: No local Python configured or found"

    def DoFind(self):
        """Run Module Finder"""

        # Figure out what Python to use
        # 1) First check configuration
        # 2) Second check for it on the path
        localpythonpath = ToolConfig.GetConfigValue(ToolConfig.TLC_PYTHON_PATH)
        if not localpythonpath:
            localpythonpath = PyToolsUtils.GetDefaultPython()

        # No configured Python
        if not localpythonpath:
            return self.nopythonerror
        util.Log("[PyFind][info] Using Python: %s" % localpythonpath)

        # No findmodule found in plugin
        if not pkg_resources.resource_exists("ModuleFinder", "findmodule.py"):
            return ["No findmodule found"]

        findmodule_script = pkg_resources.resource_filename("ModuleFinder", "findmodule.py")

        # Start find module
        finder_cmd = [localpythonpath, findmodule_script, self.moduletofind]
        util.Log("[PyFind][info] Starting command: %s" % repr(finder_cmd))
        processrunner = ProcessRunner(self.pythonpath)
        processrunner.runprocess(finder_cmd, ".")
        stdoutdata, stderrdata = processrunner.getalloutput()
        processrunner.restorepath()

        util.Log("[PyFind][info] stdout %s" % stdoutdata)
        util.Log("[PyFind][info] stderr %s" % stderrdata)
        util.Log("[PyFind][info] PyFind command finished running")
        try:
            stdoutrows = eval(stdoutdata.rstrip('\r\n'))
            rows = []
            if self.pythonpath:
                rows.append(u"INFO: Using PYTHONPATH + %s"\
                              % u", ".join(self.pythonpath))
            rows.append(u"INFO: PyFind command line: %s" % " ".join(finder_cmd))
            rows.append(u"INFO: Directory Variables file: %s" % self.dirvarfile)
            return rows + stdoutrows
        except Exception, ex:
            msg = repr(ex)
            util.Log("[PyFind][info] Error: %s" % msg)
            return [msg]
        return ["Unknown error!"]