# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_csw_explorer.ui'
#
# Created: Thu Aug 28 16:05:41 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CSW_Explorer(object):
    def setupUi(self, CSW_Explorer):
        CSW_Explorer.setObjectName(_fromUtf8("CSW_Explorer"))
        CSW_Explorer.resize(304, 659)
        font = QtGui.QFont()
        font.setUnderline(False)
        CSW_Explorer.setFont(font)
        CSW_Explorer.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelCSWURL = QtGui.QLabel(self.dockWidgetContents)
        self.labelCSWURL.setObjectName(_fromUtf8("labelCSWURL"))
        self.horizontalLayout_2.addWidget(self.labelCSWURL)
        self.comboURL = QtGui.QComboBox(self.dockWidgetContents)
        self.comboURL.setMinimumSize(QtCore.QSize(141, 0))
        self.comboURL.setEditable(True)
        self.comboURL.setObjectName(_fromUtf8("comboURL"))
        self.comboURL.addItem(_fromUtf8(""))
        self.comboURL.addItem(_fromUtf8(""))
        self.comboURL.addItem(_fromUtf8(""))
        self.comboURL.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboURL)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelKeyword = QtGui.QLabel(self.dockWidgetContents)
        self.labelKeyword.setObjectName(_fromUtf8("labelKeyword"))
        self.horizontalLayout_3.addWidget(self.labelKeyword)
        self.keywordTxt = QtGui.QLineEdit(self.dockWidgetContents)
        self.keywordTxt.setObjectName(_fromUtf8("keywordTxt"))
        self.horizontalLayout_3.addWidget(self.keywordTxt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.CSWInfoLabel = QtGui.QLabel(self.dockWidgetContents)
        self.CSWInfoLabel.setTextFormat(QtCore.Qt.PlainText)
        self.CSWInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CSWInfoLabel.setObjectName(_fromUtf8("CSWInfoLabel"))
        self.verticalLayout.addWidget(self.CSWInfoLabel)
        self.RequestsLabel = QtGui.QLabel(self.dockWidgetContents)
        self.RequestsLabel.setObjectName(_fromUtf8("RequestsLabel"))
        self.verticalLayout.addWidget(self.RequestsLabel)
        self.CSWRequestsTxt = QtGui.QTextBrowser(self.dockWidgetContents)
        self.CSWRequestsTxt.setMaximumSize(QtCore.QSize(16777215, 50))
        self.CSWRequestsTxt.setObjectName(_fromUtf8("CSWRequestsTxt"))
        self.verticalLayout.addWidget(self.CSWRequestsTxt)
        self.RecordsLabel = QtGui.QLabel(self.dockWidgetContents)
        self.RecordsLabel.setObjectName(_fromUtf8("RecordsLabel"))
        self.verticalLayout.addWidget(self.RecordsLabel)
        self.CSWRecordsTxt = QtGui.QTextBrowser(self.dockWidgetContents)
        self.CSWRecordsTxt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CSWRecordsTxt.setFont(font)
        self.CSWRecordsTxt.setObjectName(_fromUtf8("CSWRecordsTxt"))
        self.verticalLayout.addWidget(self.CSWRecordsTxt)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.exploreButton = QtGui.QPushButton(self.dockWidgetContents)
        self.exploreButton.setObjectName(_fromUtf8("exploreButton"))
        self.horizontalLayout.addWidget(self.exploreButton)
        self.maxRecordsSpinBox = QtGui.QSpinBox(self.dockWidgetContents)
        self.maxRecordsSpinBox.setMaximumSize(QtCore.QSize(75, 16777215))
        self.maxRecordsSpinBox.setMinimum(1)
        self.maxRecordsSpinBox.setMaximum(1000000)
        self.maxRecordsSpinBox.setProperty("value", 50)
        self.maxRecordsSpinBox.setObjectName(_fromUtf8("maxRecordsSpinBox"))
        self.horizontalLayout.addWidget(self.maxRecordsSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.exploreAllButton = QtGui.QPushButton(self.dockWidgetContents)
        self.exploreAllButton.setObjectName(_fromUtf8("exploreAllButton"))
        self.verticalLayout.addWidget(self.exploreAllButton)
        CSW_Explorer.setWidget(self.dockWidgetContents)

        self.retranslateUi(CSW_Explorer)
        QtCore.QMetaObject.connectSlotsByName(CSW_Explorer)

    def retranslateUi(self, CSW_Explorer):
        CSW_Explorer.setWindowTitle(_translate("CSW_Explorer", "CSW explorer", None))
        self.labelCSWURL.setText(_translate("CSW_Explorer", "CSW", None))
        self.comboURL.setItemText(0, _translate("CSW_Explorer", "http://www.magrama.es/ide/metadatos/srv/es/csw?", None))
        self.comboURL.setItemText(1, _translate("CSW_Explorer", "http://www.juntadeandalucia.es/medioambiente/geoinspire/servicios/srv/es/csw?", None))
        self.comboURL.setItemText(2, _translate("CSW_Explorer", "http://www.ideandalucia.es/catalogodeservicios/srv/es/csw?", None))
        self.comboURL.setItemText(3, _translate("CSW_Explorer", "http://www.fao.org/geonetwork/srv/en/csw?", None))
        self.labelKeyword.setText(_translate("CSW_Explorer", "Keyword(s)", None))
        self.keywordTxt.setToolTip(_translate("CSW_Explorer", "Enter keywords separated by a space", None))
        self.CSWInfoLabel.setText(_translate("CSW_Explorer", "Waiting for a search!", None))
        self.RequestsLabel.setText(_translate("CSW_Explorer", "Requests:", None))
        self.RecordsLabel.setText(_translate("CSW_Explorer", "Records:", None))
        self.exploreButton.setText(_translate("CSW_Explorer", "Explore", None))
        self.maxRecordsSpinBox.setToolTip(_translate("CSW_Explorer", "Maximum records to show", None))
        self.exploreAllButton.setText(_translate("CSW_Explorer", "Explore all records!", None))

