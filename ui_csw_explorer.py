# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_csw_explorer.ui'
#
# Created: Sat Aug 23 23:57:02 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CSW_Explorer(object):
    def setupUi(self, CSW_Explorer):
        CSW_Explorer.setObjectName(_fromUtf8("CSW_Explorer"))
        CSW_Explorer.resize(312, 629)
        font = QtGui.QFont()
        font.setUnderline(False)
        CSW_Explorer.setFont(font)
        CSW_Explorer.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.exploreButton = QtGui.QPushButton(self.dockWidgetContents)
        self.exploreButton.setGeometry(QtCore.QRect(10, 570, 211, 27))
        self.exploreButton.setObjectName(_fromUtf8("exploreButton"))
        self.CSWRecordsTxt = QtGui.QTextBrowser(self.dockWidgetContents)
        self.CSWRecordsTxt.setGeometry(QtCore.QRect(10, 270, 281, 291))
        self.CSWRecordsTxt.setObjectName(_fromUtf8("CSWRecordsTxt"))
        self.comboURL = QtGui.QComboBox(self.dockWidgetContents)
        self.comboURL.setGeometry(QtCore.QRect(50, 22, 241, 27))
        self.comboURL.setMinimumSize(QtCore.QSize(141, 0))
        self.comboURL.setEditable(True)
        self.comboURL.setObjectName(_fromUtf8("comboURL"))
        self.CSWInfoLabel = QtGui.QLabel(self.dockWidgetContents)
        self.CSWInfoLabel.setGeometry(QtCore.QRect(10, 120, 271, 17))
        self.CSWInfoLabel.setTextFormat(QtCore.Qt.PlainText)
        self.CSWInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CSWInfoLabel.setObjectName(_fromUtf8("CSWInfoLabel"))
        self.CSWRequestsTxt = QtGui.QTextBrowser(self.dockWidgetContents)
        self.CSWRequestsTxt.setGeometry(QtCore.QRect(10, 170, 281, 61))
        self.CSWRequestsTxt.setObjectName(_fromUtf8("CSWRequestsTxt"))
        self.RequestsLabel = QtGui.QLabel(self.dockWidgetContents)
        self.RequestsLabel.setGeometry(QtCore.QRect(10, 150, 66, 17))
        self.RequestsLabel.setObjectName(_fromUtf8("RequestsLabel"))
        self.RecordsLabel = QtGui.QLabel(self.dockWidgetContents)
        self.RecordsLabel.setGeometry(QtCore.QRect(10, 250, 66, 17))
        self.RecordsLabel.setObjectName(_fromUtf8("RecordsLabel"))
        self.labelCSWURL = QtGui.QLabel(self.dockWidgetContents)
        self.labelCSWURL.setGeometry(QtCore.QRect(12, 22, 32, 17))
        self.labelCSWURL.setObjectName(_fromUtf8("labelCSWURL"))
        self.labelKeyword = QtGui.QLabel(self.dockWidgetContents)
        self.labelKeyword.setGeometry(QtCore.QRect(10, 60, 81, 17))
        self.labelKeyword.setObjectName(_fromUtf8("labelKeyword"))
        self.keywordTxt = QtGui.QLineEdit(self.dockWidgetContents)
        self.keywordTxt.setGeometry(QtCore.QRect(90, 60, 201, 27))
        self.keywordTxt.setObjectName(_fromUtf8("keywordTxt"))
        self.maxRecordsSpinBox = QtGui.QSpinBox(self.dockWidgetContents)
        self.maxRecordsSpinBox.setGeometry(QtCore.QRect(230, 570, 60, 27))
        self.maxRecordsSpinBox.setMinimum(1)
        self.maxRecordsSpinBox.setMaximum(1000000)
        self.maxRecordsSpinBox.setProperty("value", 50)
        self.maxRecordsSpinBox.setObjectName(_fromUtf8("maxRecordsSpinBox"))
        CSW_Explorer.setWidget(self.dockWidgetContents)

        self.retranslateUi(CSW_Explorer)
        QtCore.QMetaObject.connectSlotsByName(CSW_Explorer)

    def retranslateUi(self, CSW_Explorer):
        CSW_Explorer.setWindowTitle(QtGui.QApplication.translate("CSW_Explorer", "CSW explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.exploreButton.setText(QtGui.QApplication.translate("CSW_Explorer", "Explore", None, QtGui.QApplication.UnicodeUTF8))
        self.CSWInfoLabel.setText(QtGui.QApplication.translate("CSW_Explorer", "Waiting for a search!", None, QtGui.QApplication.UnicodeUTF8))
        self.RequestsLabel.setText(QtGui.QApplication.translate("CSW_Explorer", "Requests:", None, QtGui.QApplication.UnicodeUTF8))
        self.RecordsLabel.setText(QtGui.QApplication.translate("CSW_Explorer", "Records:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCSWURL.setText(QtGui.QApplication.translate("CSW_Explorer", "CSW", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKeyword.setText(QtGui.QApplication.translate("CSW_Explorer", "Keyword(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.keywordTxt.setToolTip(QtGui.QApplication.translate("CSW_Explorer", "Enter keywords separated by a space", None, QtGui.QApplication.UnicodeUTF8))
        self.maxRecordsSpinBox.setToolTip(QtGui.QApplication.translate("CSW_Explorer", "Maximum records to show", None, QtGui.QApplication.UnicodeUTF8))

