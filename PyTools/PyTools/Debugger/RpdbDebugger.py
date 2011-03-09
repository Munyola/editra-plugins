# -*- coding: utf-8 -*-
# Name: RpdbDebugger.py
# Purpose: Debug Client
# Author: Mike Rans
# Copyright: (c) 2010 Mike Rans
# License: wxWindows License
##############################################################################
""" RpdbDebugger functions """

__version__ = "0.2"
__author__ = "Mike Rans"
__svnid__ = "$Id: RpdbDebugger.py 1025 2010-12-24 18:30:23Z rans@email.com $"
__revision__ = "$Revision: 1025 $"

#-----------------------------------------------------------------------------#
# Editra Libraries
import util

# Local Imports
import rpdb2
from PyTools.Debugger.RpdbStateManager import RpdbStateManager
from PyTools.Debugger.RpdbBreakpointsManager import RpdbBreakpointsManager
from PyTools.Debugger.RpdbStackFrameManager import RpdbStackFrameManager
from PyTools.Debugger.RpdbThreadsManager import RpdbThreadsManager
from PyTools.Debugger.RpdbVariablesManager import RpdbVariablesManager

#----------------------------------------------------------------------------#

class RpdbDebugger(object):
    fAllowUnencrypted = True
    fRemote = False
    host = "localhost"
    fAttach = True
    fchdir = False
    password = "editra123"

    def __init__(self):
        super(RpdbDebugger, self).__init__()
        self.sessionmanager = rpdb2.CSessionManager(RpdbDebugger.password, \
            RpdbDebugger.fAllowUnencrypted, RpdbDebugger.fRemote, RpdbDebugger.host)
        self.breakpointmanager = RpdbBreakpointsManager(self)
        self.statemanager = RpdbStateManager(self)
        self.stackframemanager = RpdbStackFrameManager(self)
        self.threadmanager = RpdbThreadsManager(self)
        self.variablesmanager = RpdbVariablesManager(self)
        
        # attributes that will be set later
        self.pid = None
        self.mainwindowid = None
        self.breakpoints_loaded = False
        self.curstack = None
        
        # functions that will be set later
        
        # debuggee shelf
        self.debuggeroutput = None
        # breakpoint shelf
        self.getbreakpoints = None
        # stackframe shelf
        self.clearstepmarker = None
        self.setstepmarker = None
        self.checkterminate = None
        self.clearframe = None
        self.selectframe = None
        self.updatestacklist = None
        # thread shelf
        self.clearthread = None
        self.updatethread = None
        self.updatethreadlist = None
        # variables shelf
        self.clearlocalvariables = None
        self.clearglobalvariables = None
        self.clearexceptions = None
        self.updatelocalvariableslist = None
        self.updateglobalvariableslist = None
        self.updateexceptionslist = None

    def clear_all(self):
        self.clearstepmarker()
        self.clearlocalvariables()
        self.clearglobalvariables()
        self.clearexceptions()
        self.clearframe()
        self.clearthread()

    def attach(self):
        if self.pid:
            util.Log("[PyDbg][info] Trying to Attach")    
            self.sessionmanager.attach(self.pid, encoding = rpdb2.detect_locale())
            util.Log("[PyDbg][info] Running")
            self.pid = None

    def do_detach(self):
        try:
            self.sessionmanager.detach()
        except rpdb2.NotAttached:
            pass

    def register_callback(self, func, event_type_dict, fSingleUse = False):
        self.sessionmanager.register_callback(func, event_type_dict, fSingleUse = fSingleUse)

    def set_frameindex(self, index):
        try:
            self.sessionmanager.set_frame_index(index)        
        except rpdb2.NotAttached:
            pass
            
    def get_frameindex(self):
        try:
            return self.sessionmanager.get_frame_index()        
        except rpdb2.NotAttached:
            pass
        return None
            
    def do_stop(self):
        try:
            self.sessionmanager.stop_debuggee()
        except rpdb2.NotAttached:
            pass

    def do_restart(self):
        try:
            self.sessionmanager.restart()
        except rpdb2.NotAttached:
            pass

    def do_jump(self, lineno):
        try:
            self.sessionmanager.request_jump(lineno)
        except rpdb2.NotAttached:
            pass

    def do_go(self):
        try:
            self.sessionmanager.request_go()
        except rpdb2.NotAttached:
            pass

    def do_break(self):
        try:
            self.sessionmanager.request_break()
        except rpdb2.NotAttached:
            pass

    def do_step(self):
        try:
            self.sessionmanager.request_step()
        except rpdb2.NotAttached:
            pass

    def do_next(self):
        try:
            self.sessionmanager.request_next()
        except rpdb2.NotAttached:
            pass

    def do_return(self):
        try:
            self.sessionmanager.request_return()
        except rpdb2.NotAttached:
            pass

    def run_toline(self, filename, lineno):
        try:
            self.sessionmanager.request_go_breakpoint(filename, '', lineno)
        except rpdb2.NotAttached:
            pass

    def disable_breakpoint(self, bpid):
        try:
            self.sessionmanager.disable_breakpoint([bpid], True)
        except rpdb2.NotAttached:
            pass

    def enable_breakpoint(self, bpid):
        try:
            self.sessionmanager.enable_breakpoint([bpid], True)
        except rpdb2.NotAttached:
            pass

    def clear_breakpoints(self):
        try:
            self.sessionmanager.delete_breakpoint([], True)
        except rpdb2.NotAttached:
            pass
        
    def set_breakpoint(self, filepath, lineno, exprstr = "", enabled=True):
        try:
            return self.sessionmanager.set_breakpoint(filepath, '', lineno, enabled, exprstr)
        except rpdb2.NotAttached:
            return None

    def delete_breakpoint(self, bpid):
        try:
            self.sessionmanager.delete_breakpoint([bpid], True)
        except rpdb2.NotAttached:
            pass

    def load_breakpoints(self):
        try:
            self.sessionmanager.load_breakpoints()
        except rpdb2.NotAttached:
            pass

    def update_variableslists(self):
        self.curstack
        self.updatelocalvariableslist(variables)
        self.updateglobalvariableslist(variables)
        self.updateexceptionslist(variables)

