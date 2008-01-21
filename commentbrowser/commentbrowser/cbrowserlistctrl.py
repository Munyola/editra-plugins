###############################################################################
# Name:  cbrowserlistctrl.py                                                  #
# Purpose: a simple to use listctrl for todo tasks                            #
# Author: DR0ID <dr0iddr0id@googlemail.com>                                   #
# Copyright: (c) 2007 DR0ID                                                   #
# Licence: wxWindows Licence                                                  #
###############################################################################

"""
Provides a virtual ListCtrl for the CommentBrowser
"""

__author__ = "DR0ID"
__svnid__ = "$Id: Exp $"
__revision__ = "$Revision$"

#------------------------------------------------------------------------------#
# Imports
import sys
import locale
import wx
import wx.lib.mixins.listctrl as listmix

#Editra Library Modules
import ed_glob

#------------------------------------------------------------------------------#
# Globals


_ = wx.GetTranslation

#------------------------------------------------------------------------------#



class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin,
            listmix.ColumnSorterMixin):

    """The list ctrl used for the list"""

    def __init__(
        self,
        parent,
        ID=-1,
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=wx.BORDER_NONE|wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES|wx.LC_SINGLE_SEL|wx.LC_VIRTUAL|wx.LC_SORT_DESCENDING):
        """Init the TestListCtrl"""

        self._log('TestListCtrl before init base classes')
        wx.ListCtrl.__init__(
            self,
            parent,
            ID,
            pos,
            size,
            style,
            )

        #---- Images used by the list ----#
        isize = (8, 8)
        self._img_list = wx.ImageList(*isize)
        
        up = wx.ArtProvider_GetBitmap(str(ed_glob.ID_UP), wx.ART_MENU, isize)
        if not up.IsOk():
            up = wx.ArtProvider_GetBitmap(wx.ART_GO_UP, wx.ART_TOOLBAR, isize)
        self.sm_up = self._img_list.Add(up)

        down = wx.ArtProvider_GetBitmap(str(ed_glob.ID_DOWN), wx.ART_MENU, isize)
        if not down.IsOk():
            down = wx.ArtProvider_GetBitmap(wx.ART_GO_DOWN, wx.ART_TOOLBAR, isize)
        self.sm_dn = self._img_list.Add(down)

        self.SetImageList(self._img_list, wx.IMAGE_LIST_SMALL)

        #---- Set Columns Headers ----#
        self.InsertColumn(0, "!")
        self.InsertColumn(1, _("Type"))
        self.InsertColumn(2, _("Description"))
        self.InsertColumn(3, _("File"))
        self.InsertColumn(4, _("Line"))

        self.SetColumnWidth(0, 38)
        self.SetColumnWidth(1, 59)
        self.SetColumnWidth(2, 429)
        self.SetColumnWidth(3, 117)

        #---- data ----#
        #this attribute ist required by listmix.ColumnSorterMixin
        #{1:(prio, task, description, file, line, fullname), etc.}
        self.itemDataMap = {}
        # [key1, key2, key3, ...]
        self.itemIndexMap = self.itemDataMap.keys()
        self.SetItemCount(len(self.itemDataMap))

        # needed to hold a reference (otherwise it would be 
        # garbagecollected too soon causing a crash)
        self._attr = None 

        # TODO: prio colors
#        self._max_prio = 0 
#        self._prio_colors = [] # min 2 colors!!
#        # assume _max_prio = 10, len(prio_colors) = 4 -> 10//(4-1) = 10//3 = 3
#        # coloridx for given prio: cidx = int(prio//3)

        #---- init base classes ----#
        # hast to be after self.itemDataMap has been initialized and the
        # setup of the columns, but befor sorting
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        listmix.ColumnSorterMixin.__init__(self, 5)

        #---- Events ----#
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnItemRightClick, self)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated, self)

#        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self)
#        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected, self)
#        self.Bind(wx.EVT_LIST_DELETE_ITEM, self.OnItemDelete, self)
#        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self)
#        self.Bind(wx.EVT_LIST_COL_RIGHT_CLICK, self.OnColRightClick, self)
#        self.Bind(wx.EVT_LIST_COL_BEGIN_DRAG, self.OnColBeginDrag, self)
#        self.Bind(wx.EVT_LIST_COL_DRAGGING, self.OnColDragging, self)
#        self.Bind(wx.EVT_LIST_COL_END_DRAG, self.OnColEndDrag, self)
#        self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnBeginEdit, self)
#        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick, self)
#        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown, self)
        #for wxMSW
#        self.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick, self)
        #for wxGTK
#        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClick, self)


        #sort by prio (column 0), descending order (0)
        self.SortListItems(0, 0)

        
    #---- methods ----#

    def _log(self, msg):
        """Private log method of this class"""
        wx.GetApp().GetLog()('>>>>>>>>>>>>>>[commentbrowser][listctr] '
                              + str(msg))

    def AddEntry(
        self,
        prio,
        tasktype,
        descr,
        file,
        line,
        fullname,
        refresh = True
        ):
        """Add a entry to the list"""
        # add to itemDataMap for sorting
        val = (int(prio), str(tasktype), str(descr), str(file), int(line), str(fullname))
        # XXX: how to do a better datastructure to save data (and only update partial data)
        key = hash(val)
        self.itemDataMap[key] = val
        # TODO: perhaps add it in a sorted manner (if possible, dont know)
        self.itemIndexMap = list(self.itemDataMap.keys())
        self.SetItemCount(len(self.itemDataMap))
        if refresh:
            self.Refresh()
        
        self._log("itemcount Add entry "+str(self.GetItemCount())+" key:"+str(key))
        return key
        
    def AddEntries(self, entrylist):
        """Adds all entries from the entrylist. The entries must be a tuple
        containing (prio, tasktype, description, file, line, fullname)"""
        keys = []
        for entry in entrylist:
            prio, task, descr, file, line , fullname = entry
            keys.append(self.AddEntry(prio, task, descr, file, line, fullname, refresh=False))
        self.SetItemCount(len(self.itemDataMap))
#        self.Refresh()
        return keys
        
    def RemoveEntry(self, key):
        """Removes a entry identified by its key"""
        self.itemDataMap.pop(key, None)
        self.itemIndexMap = list(self.itemDataMap.keys())
        self.SetItemCount(len(self.itemDataMap))
#        self.Refresh()
        
    def Clear(self, keys=None, refresh=True):
        """Removes all entries from list"""
        if keys is None:
            self.itemDataMap.clear()
            self.itemIndexMap = list(self.itemDataMap.keys())
            self.SetItemCount(len(self.itemDataMap))
            if refresh:
                self.Refresh()
        else:
            for key in keys:
                self.RemoveEntry(key)
    
    # TODO: new "delta data" update method, once implemented 
    #       delete AddEntry, AddEntries, RemoveEntry and Clear
    # appendEntries = [(key, data), ... ]
    # removeEntries = [key1, key2, ...]
    def UpdateEntries(self, appendEntries=[], removeEntries=[]):
        pass
        
    def GetEntriesKeys(self):
        return self.itemDataMap.keys()

    def NavigateToTaskSource(self, itemIndex):
    
        if itemIndex < 0 or itemIndex > len(self.itemDataMap):
            self._log('[error] itemIndex out of range!')
            return
        
        key = self.itemIndexMap[itemIndex]
        source = str(self.itemDataMap[key][-1])
        line = self.itemDataMap[key][-2]
        try:
            nb = self.GetParent().GetParent().GetNotebook()
            ctrls = nb.GetTextControls()
            for ctrl in ctrls:
                if source == ctrl.GetFileName() :
                    nb.SetSelection(nb.GetPageIndex(ctrl))
                    nb.GoCurrentPage()
                    ctrl.GotoLine(line-1)
                    break;
        except Exception, e:
            self._log("[error] "+e.msg)


    #---- special methods used by the mixinx classes ----#
    
    #Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        """ this method is required by listmix.ColumnSorterMixin"""
        return self

    #---------------------------------------------------
    #Matt C, 2006/02/22
    #Here's a better SortItems() method --
    #the ColumnSorterMixin.__ColumnSorter() method already handles the ascending/descending,
    #and it knows to sort on another column if the chosen columns have the same value.
    def SortItems(self, sorter=cmp):
        """
        This method is required by the 
        wx.lib.mixins.listctrl.ColumnSorterMixin, for internal usage only
        """
        sorter = self.__ColumnSorter
        items = list(self.itemDataMap.keys())
        items.sort(sorter)
        self.itemIndexMap = items

        #redraw the list
#        self.Refresh()
        
    def GetColumnSorter(self):
        self._log('GetColumnSorter')
        return self.__ColumnSorter

    def GetSecondarySortValues(self, col, key1, key2):
        self._log('GetSecondarySortValues: col: %d  key1: %d   key2: %d'%(col, key1, key2))
        cmpVal = __ColumnSorter(key1, key2)
        if 0 < cmpVal:
            return (key2, key1)
        return (key1, key2)
        
        
    def __ColumnSorter(self, key1, key2):
        col = self._col
        ascending = self._colSortFlag[col]
        self._log('__ColumnSorter: col: %d  asc: %d'%(col, ascending))
        #{1:(prio, task, description, file, line, fullname), etc.}
        if 0 == col: # prio -> sortorder: prio task file line
            _sortorder = [col, 1, 3, 4]
        elif 1 == col: # task -> sortorder: task prio, file , line
            _sortorder = [col, 0, 3, 4]
        elif 2 == col: # descr -> sortorder: descr, prio, task
            _sortorder = [col, 0, 1, 3, 4]
        elif 3 == col : # file -> sortorder: file, prio line
            _sortorder = [col, 0, 4]
        elif 4 == col: # line number -> sortorder: file, line
            _sortorder = [3, 4]
            
        cmpVal = 0
        _idx = 0
        while( 0 == cmpVal and _idx < len(_sortorder) ):
            item1 = self.itemDataMap[key1][ _sortorder[_idx] ]
            item2 = self.itemDataMap[key2][ _sortorder[_idx] ]
            #--- Internationalization of string sorting with locale module
            if type(item1) == type('') or type(item2) == type(''):
                cmpVal = locale.strcoll(str(item1), str(item2))
            else:
                cmpVal = cmp(item1, item2)
            #---
            _idx += 1

        # in certain cases always ascending/descending order is prefered
        if 0 == _sortorder[_idx-1] and 0 != col:
            ascending = 0
#        elif 0 == _sortorder[_idx-1] and 0 == col:
#            ascending = ascending ^ 1
        elif 4 == _sortorder[_idx-1] and 4 != col:
            ascending = 1
        elif 3 == _sortorder[_idx-1] and 4 == col:
            ascending = 1
            
        if ascending:
            return cmpVal
        else:
            return -cmpVal

    #Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetSortImages(self):
        """
        This method is required by the 
        wx.lib.mixins.listctrl.ColumnSorterMixin, for internal usage only
        """
        return (self.sm_dn, self.sm_up)
        
    #---- special listctrl eventhandlers ----#
        # These methods are callbacks for implementing the
        # "virtualness" of the list...

    def OnGetItemText(self, itemIdx, col):
        """
        Virtual ListCtrl have to define this method, returns the text of the
        requested item
        """
        index = self.itemIndexMap[itemIdx]
        s = self.itemDataMap[index][col]
        return s

    def OnGetItemImage(self, item):
        """
        Virtual ListCtrl have to define this method, should return an image
        for the item, but since we have no images it always returns -1.
        """
        return -1

    def OnGetItemAttr(self, itemIdx):
        """
        Virtual ListCtrl have to define this method, should return item 
        attributes, but since we have none it always returns None.
        """
        # TODO: set some color depending on priority
#        self._attr = wx.ListItemAttr(wx.NullColor, wx.Color(255, 255, 0), wx.NullFont)
#        return self._attr
        return None

    #---- Eventhandler ----#

    def OnItemDeselected(self, event):
        self._log('OnItemDeselected')
#        item = event.GetItem()
        self._log("OnItemDeselected: %d" % event.m_itemIndex)

    def OnItemActivated(self, event):
        self._log('OnItemActivated')
        self.NavigateToTaskSource(event.m_itemIndex)

    def OnItemRightClick(self, event):
        self.NavigateToTaskSource(event.m_itemIndex)
        event.Skip()


#    def OnItemSelected(self, event):
#        self._log('OnItemSelected')
#        event.Skip()

#    def OnItemDelete(self, event):
#        self._log('OnItemDelete')

#    def OnColClick(self, event):
#        self._log('OnColClick '+str(event.GetColumn()))
#        event.Skip()

#    def OnSortOrderChanged(self):
#        self._log('OnSortOrderChanged')

#    def OnColRightClick(self, event):
#        self._log('OnColRightClick')

#    def OnColBeginDrag(self, event):
#        self._log('OnColBeginDrag')

#    def OnColDragging(self, event):
#        self._log('OnColDragging')

#    def OnColEndDrag(self, event):
#        self._log('OnColEndDrag')
#        for colnum in [0, 1, 2, 3]:
#            self._log(self.GetColumnWidth(colnum))

#    def OnBeginEdit(self, event):
#        self._log('OnBeginEdit')

#    def OnDoubleClick(self, event):
#        self._log('OnDoubleClick'+str(event))
#        # OnItemSelected is called first, so self._currentItemIdx is already set
#        self.NavigateToTaskSource(self._currentItemIdx)
#        event.Skip()
        

#    def OnRightDown(self, event):
#        self._log('OnRightDown')
#        event.Skip()

#    def OnRightClick(self, event):
#        self._log('OnRightClick')
#        event.Skip()

        
    

