############################################################################
#    Copyright (C) 2007 Cody Precord                                       #
#    cprecord@editra.org                                                   #
#                                                                          #
#    Editra is free software; you can redistribute it and#or modify        #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    Editra is distributed in the hope that it will be useful,             #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################

"""
#--------------------------------------------------------------------------#
# FILE: diffwin.py
# AUTHOR: Cody Precord
# LANGUAGE: Python
# SUMMARY:
#
#
# METHODS:
#
#
#
#--------------------------------------------------------------------------#
"""

__author__ = "Cody Precord <cprecord@editra.org>"
__cvsid__ = "$Id$"
__revision__ = "$Revision$"

#--------------------------------------------------------------------------#
# Dependancies
import wx
import os
import tempfile
import webbrowser

# Local libs
import difflib

# Editra libs
import ed_stc
import util
from extern import flatnotebook as FNB
from profiler import Profile_Get
#--------------------------------------------------------------------------#

class DiffWindow(wx.Frame):
    """Creates a window for displaying file diffs"""
    def __init__(self, parent, id, title):
        """Initialize the Window"""
        wx.Frame.__init__(self, parent, id, title, size=(300, 300))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._book = DiffBook(self)
        sizer.Add(self._book, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

    def OpenDiffs(self, flist):
        """Open a list of diffed files
        @param flist: list of file paths
        @type flist: [(a1, a2), (b1, b2), ...]

        """
        self._book.OpenFiles(flist)

#--------------------------------------------------------------------------#

class DiffBook(FNB.FlatNotebook):
    """Notebook for holding multiple diff panels"""
    def __init__(self, parent):
        """Initialize the book"""
        FNB.FlatNotebook.__init__(self, parent) 
                                  style=FNB.FNB_FF2 | \
                                        FNB.FNB_HIDE_ON_SINGLE_TAB | \
                                        FNB.FNB_X_ON_TAB)
        FNB.FlatNotebook.AddPage(self, wx.Panel(self, size=(200, 200)), "tmp")
        # Attributes
        self.log = wx.GetApp().GetLog()

    def OpenFiles(self, flist):
        """Open a list of files is separate pages
        @param flist: list of tuples containing file paths
        @type flist: [(path2left, path2right), (p2l, p2r), ...]

        """
        for pair in flist:
            panel = DisplayPanel(self, pair[0], pair[1])
            FNB.FlatNotebook.AddPage(self, panel, os.path.basename(pair[0]))

    def OpenDiffTxt(self, txtlst):
        """Open a list of diff results in separate pages"""
#--------------------------------------------------------------------------#

class DisplayPanel(wx.Panel):
    """Creates a panel for displaying the diff in a side by side"""
    def __init__(self, parent, left, right):
        """Create the diff panel
        @param parent: parent window of this panel
        @param left: path to left file
        @param right: path to right file

        """
        wx.Panel.__init__(self, parent)
        
        # Attributes
        self._log = wx.GetApp().GetLog()
        self._left = (left, DiffCtrl(self))
        self._left[1].SetUseVerticalScrollBar(False)
        self._right = (right, DiffCtrl(self))
        self._difftxt = self.Generate()
        
        # Layout panel
        self._DoLayout()
        self._PopulateCtrls()

        # Event Handlers
        self._right[1].Bind(wx.EVT_SCROLLWIN, self.OnScroll)

    def _DoLayout(self):
        """Layout the window"""
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self._left[1], 1, wx.EXPAND | wx.ALIGN_LEFT)
        sizer.Add(self._right[1], 1, wx.EXPAND | wx.ALIGN_RIGHT)
        self.SetSizer(sizer)
        self.SetInitialSize()

    def _PopulateCtrls(self):
        """Populate the text ctrls"""
        ltxt = GetLines(self._left[0])
        if ltxt != -1:
            for line in ltxt:
                self._left[1].AppendLine(line)
        rtxt = GetLines(self._right[0])
        if rtxt != -1:
            for line in rtxt:
                self._right[1].AppendLine(line)
        self._left[1].SetReadOnly(True)
        self._right[1].SetReadOnly(True)

    def Generate(self):
        """Generate the diff text from the displays left/right files
        and refresh the display.

        """
        diff = GenerateDiff(self._left[0], self._right[0])
        if isinstance(diff, int):
            if diff == ERR_DIFF_LFAILED:
                fname = self._left[0]
            else:
                fname = self._right[0]
            self._log("[diffwin][err] Failed to open %s" % fname)
        else:
            self._difftext = diff

    def OnScroll(self, evt):
        """Make both windows have matching scroll position"""
        pos = self._right[1].GetScrollPos(wx.VERTICAL)
        self._left[1].SetScrollPos(wx.VERTICAL, pos)
#         self._left[1].ScrollWindow(0, pos)
        self._left[1].Refresh()
        self._left[1].Update()
#         evt.Skip()
#--------------------------------------------------------------------------#
class DiffCtrl(ed_stc.EDSTC):
    """Custom text control for displaying diff files in"""
    def __init__(self, parent):
        ed_stc.EDSTC.__init__(self, parent, wx.ID_ANY, use_dt=False)
        
        # Configure the control
        self.FoldingOnOff(False)
#         self.SetReadOnly(True)

    def AppendLine(self, line):
        """Adds a line to the control. The line is checked
        for being a minus/plus line and colored properly for
        the context.

        """
        self.AppendText(line)

#--------------------------------------------------------------------------#
# Utility Functions

_tmpfiles = list()
ERR_DIFF_LFAILED = -1
ERR_DIFF_RFAILED = -2
# Unfortunatly wx.html.HtmlWindow does not handle the css generated
# by difflib so this will use an external webbrowser till wx.webkit
# is ready.
def GenerateDiff(left, right, tabwidth=8, html=False):
    """Generate the delta between the two files.
    @param left: path to left file
    @param right: path to right file
    @keyword tabwidth: tab stop spacing (only for html mode)
    @keyword html: If set to True the diff will be generated as HTML and
                   opened as a new tab in the systems webbrowser.

    """
    # Get Lines to diff
    lfile = GetLines(left)
    if lfile == -1:
        return ERR_DIFF_LFAILED

    rfile = GetLines(right)
    if rfile == -1:
        return ERR_DIFF_RFAILED

    if html:
        gen = difflib.HtmlDiff(tabwidth)
        diff = gen.make_file(lfile, rfile, left, right)
        tmp, name = tempfile.mkstemp('editra_projects_diff')
        _tmpfiles.append(name)
        tmp = file(name, 'wb')
        tmp.write(diff)
        tmp.close()
        webbrowser.open_new_tab(name)
    else:
        return list(difflib.Differ().compare(lfile, rfile))

def CleanupTempFiles(self):
    """Cleanup all temporary diff files"""
    for tmp in _tmpfiles:
        try:
            os.remove(tmp)
        except OSError:
            pass

def GetLines(fname):
    """Gets all the lines from the given file
    @return: list of lines or -1 on error

    """
    reader = util.GetFileReader(fname)
    try:
        lines = reader.readlines()
    except (AttributeError, IOError, OSError), msg:
        print msg
        return -1
    reader.close()
    return lines
