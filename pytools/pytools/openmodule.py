###############################################################################
# Name: openmodule.py                                                         #
# Purpose:                                                                    #
# Author: Rudi Pettazzi <rudi.pettazzi@gmail.com>, Ofer Schwarz               #
# Copyright: (c) 2009 Cody Precord <staff@editra.org>                         #
# License:                                                                    #
###############################################################################

"""Open module Dialog"""

__author__ = ""
__svnid__ = "$Id$"
__revision__ = "$Revision$"

#-----------------------------------------------------------------------------#
# Imports
import wx
import sys
import os.path
import finder

ID_OPEN_MODULE = wx.NewId()

#-----------------------------------------------------------------------------#
# Globals
_ = wx.GetTranslation

#-----------------------------------------------------------------------------#

class OpenModuleDialog(wx.Dialog):
    """ A dialog to find the source file of a module and open it into the
    editor notebook
    """

    def __init__(self, parent, finder, *args, **kwargs):
        """Open the dialog.
        @param parent: the parent window
        @param finder: an instance of finder.ModuleFinder
        """
        wx.Dialog.__init__(self, parent, wx.ID_ANY,
                           style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER,
                           size=(400, 230), *args, **kwargs)

        # Attributes
        self.finder = finder
        self.search = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.search.ShowCancelButton(True)
        self.btnOk = wx.Button(self, wx.ID_OK, label=_('Ok'))
        self.btnOk.Enable(False)
        self.btnCancel = wx.Button(self, wx.ID_CANCEL, label=_('Cancel'))
        self.listBox = wx.ListBox(self)

        # Layout
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_TEXT_ENTER, self.OnSearch, self.search)
        self.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnCancelSearch, self.search)
        self.Bind(wx.EVT_BUTTON, self.OnConfirm, self.btnOk)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnConfirm, self.listBox)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, self.btnCancel)

    def __DoLayout(self):
        """Layout the dialog"""
        label1 = wx.StaticText(self, label=_('Find and open a module by name'))
        labsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        labsizer1.Add(label1, 1, wx.ALL, 5)

        txtsizer = wx.BoxSizer(wx.HORIZONTAL)
        txtsizer.Add(self.search, 1, wx.ALL, 5)

        dsizer = wx.BoxSizer(wx.HORIZONTAL)
        divider = wx.StaticLine(self, size=(-1, 1))
        dsizer.AddMany([((5, 5), 0), (divider, 1), ((5, 5), 0)])

        label2 = wx.StaticText(self, label=_('Matching items') + u":")
        labsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        labsizer2.Add(label2, 1, wx.ALL, 5)

        lstsizer = wx.BoxSizer(wx.HORIZONTAL)
        lstsizer.Add(self.listBox, 1, wx.ALL|wx.EXPAND, 5)
        lstvsizer = wx.BoxSizer(wx.VERTICAL)
        lstvsizer.Add(lstsizer, 1, wx.EXPAND)

        bsizer = wx.StdDialogButtonSizer()
        bsizer.AddButton(self.btnOk)
        bsizer.AddButton(self.btnCancel)
        bsizer.Realize()

        mainsizer = wx.BoxSizer(wx.VERTICAL)
        mainsizer.AddMany([(labsizer1, 0), (txtsizer, 0, wx.EXPAND),
                            ((5, 5), 0),
                            (dsizer, 0, wx.EXPAND), ((5, 5), 0),
                            (labsizer2, 0),
                            (lstvsizer, 2, wx.EXPAND), (bsizer, 0, wx.EXPAND),
                            ((5, 5), 0)])

        self.SetSizer(mainsizer)

    def GetValue(self):
        return self.result

    def OnConfirm(self, evt):
        n = self.listBox.GetSelection()
        if n >= 0:
            self.result = self.listBox.GetString(n)
            self.EndModal(wx.ID_OK)

    def OnCancel(self, evt):
        self.result = None
        self.EndModal(wx.ID_CANCEL)

    def OnCancelSearch(self, evt):
        self.search.SetValue('')
        self.listBox.Set([])
        self.btnOk.Enable(False)

    def OnSearch(self, evt):
        """Handle search events from the SearchCtrl"""
        self.listBox.Set([])
        files = self.finder.Find(self.search.GetValue())
        self.listBox.Set(files)
        if len(files):
            self.listBox.SetSelection(0)
            self.btnOk.Enable(True)

#-----------------------------------------------------------------------------#
# Test
class MyApp(wx.App):
    def OnInit(self):
        mf = finder.ModuleFinder(finder.GetSearchPath())
        dialog = OpenModuleDialog(None, mf, title=_("Open module"))
        filename = None
        if dialog.ShowModal() == wx.ID_OK:
            filename = dialog.GetValue()
        if dialog:
            dialog.Destroy()
        return True

if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()

