# -*- coding: utf-8 -*-
"""
***************************************************************************
 CSW_Explorer
 A QGIS plugin
 Retrieving info from a CSW with OWSLib
                             -------------------
        begin                : 2014-08-16
        copyright            : (C) 2014 by Geographica
        email                : cayetano.benavent@geographica.gs
***************************************************************************

***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from PyQt4 import QtCore, QtGui
from ui_csw_explorer import Ui_CSW_Explorer


class CSW_ExplorerDialog(QtGui.QDockWidget, Ui_CSW_Explorer):
    # create the dock dialog
    def __init__(self):
        QtGui.QDockWidget.__init__(self)
        # Set up the user interface from Designer
        self.setupUi(self)
    
    def setTextRecords(self, text_output):
        self.CSWRecordsTxt.setText(text_output)

    def clearTextRecords(self):
        self.CSWRecordsTxt.clear()
    
    def setTextRequests(self, text_output):
        self.CSWRequestsTxt.setText(text_output)

    def clearTextRequests(self):
        self.CSWRequestsTxt.clear()
    
    def getComboURL(self):
        return self.comboURL.currentText()

    def getKeyword(self):
        return self.keywordTxt.text()
    
    def getMaxRecordToShow(self):
        return self.maxRecordsSpinBox.value()
    
    def setInfoLabel(self, text_output):
        self.CSWInfoLabel.setText(text_output)
    
    def enableExploreAllButton(self):
        self.exploreAllButton.setEnabled(True)
    
    def disableExploreAllButton(self):
        self.exploreAllButton.setEnabled(False)
