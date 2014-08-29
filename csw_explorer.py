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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt resources from file resources.py
import resources_rc

# Import the code for the dialog
from csw_explorerdialog import CSW_ExplorerDialog

# Import Python built-in libraries
import sys
import os.path

# Import other libraries
from owslib.csw import CatalogueServiceWeb


class CSW_Explorer:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'csw_explorer_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dock dialog (after translation) and keep reference
        self.dockdlg = CSW_ExplorerDialog()
        
        #Total records var
        self.totalrecords = 0

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/csw_explorer/icon.png"),
            u"CSW Explorer", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&CSW Explorer", self.action)

        # Add dock dialog to the right
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockdlg)

        # Connecting actions and functions (signals and slots)
        QObject.connect(self.dockdlg.exploreButton, SIGNAL("clicked()"), self.exploreCSW)
        QObject.connect(self.dockdlg.exploreAllButton, SIGNAL("clicked()"), self.exploreAllCSW)
        
        #Disable Explore all records button
        self.dockdlg.disableExploreAllButton()

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&CSW Explorer", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        # Show the dock dialog
        self.dockdlg.show()
    
    def changeInfoLabel(self, text_output):
        self.dockdlg.setInfoLabel(text_output)
    
    def getRecords(self, maxrecordstoshow):
        """
        Get records in a CSW catalog
            
            CSW examples:
            
                csw_list = [
                "http://www.magrama.es/ide/metadatos/srv/es/csw?",
                "http://www.ideandalucia.es/catalogodeservicios/srv/es/csw?",
                "http://www.juntadeandalucia.es/medioambiente/geoinspire/servicios/srv/es/csw?",
                "http://www.fao.org/geonetwork/srv/en/csw?"
                ]
        """
        
        self.dockdlg.clearTextRecords()
        self.dockdlg.clearTextRequests()
        
        cswRecords = ""
        cswRequests = ""
        
        # Get the CSW url to explore from combobox
        csw_catalog = self.dockdlg.getComboURL()
        
        if not csw_catalog:
            self.iface.messageBar().pushMessage("Warning", "Enter a valid CSW URL", level=QgsMessageBar.WARNING)
            self.changeInfoLabel("There is not a CSW URL")
        else:
            # If there is a keyword, will be used
            keywords = self.dockdlg.getKeyword()
            # Set the catalog web service
            csw = CatalogueServiceWeb(csw_catalog, timeout=300)
            
            # Getting records...
            csw.getrecords(keywords=keywords.split(), maxrecords=maxrecordstoshow)
            
            #osw_type = csw.identification.type
            
            for op in csw.operations:
                # listing available operations
                cswRequests += "- %s\n" % (op.name)
                        
            for rec in csw.records:
                # listing records titles
                cswRecords += "- %s\n" % (csw.records[rec].title)
            
            self.iface.messageBar().pushMessage("Finished search for: ", csw_catalog, duration=4)
            
            res_matches = csw.results['matches']
            res_returned = csw.results['returned']
            
            self.changeInfoLabel("Results: %s  /  Showed: %s" % (res_matches, res_returned))
            self.dockdlg.setTextRecords(cswRecords)
            self.dockdlg.setTextRequests(cswRequests)

            return res_matches, res_returned
            
    def exploreCSW(self):
        """
        Explore a CSW catalog

        """
        
        # Set a maximum number of records to retrieve
        maxrecordstoshow = self.dockdlg.getMaxRecordToShow()
        
        try:
            res_matches, res_returned = self.getRecords(maxrecordstoshow)
            
            if res_matches > res_returned:
                #Enable Explore all records button
                self.dockdlg.enableExploreAllButton()
                self.totalrecords = res_matches
            
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.iface.messageBar().pushMessage("Error", str(exc_value), level=QgsMessageBar.CRITICAL)
            self.changeInfoLabel("Enter a valid CSW URL!")
    
    def exploreAllCSW(self):
        """
        Explore all records...
        
        If there are more match records than maximum records to show
        you can use this functionality

        """
        
        try:
            self.getRecords(self.totalrecords)

        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.iface.messageBar().pushMessage("Error", str(exc_value), level=QgsMessageBar.CRITICAL)
            self.changeInfoLabel("Enter a valid CSW URL!")
        
        #Disable Explore all records button
        self.dockdlg.disableExploreAllButton()


