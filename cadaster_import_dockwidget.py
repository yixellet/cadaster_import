# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CadasterImportDockWidget
                                 A QGIS plugin
 Imports XML files from russian state land register
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-02-03
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Kirill Kotelevsky
        email                : thaid@yandex.ru
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import

import os

from qgis import gui
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal, QCoreApplication

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'cadaster_import_dockwidget_base.ui'))


class CadasterImportDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(CadasterImportDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
    
    def on_importToDB_toggled(self):
        self.dbFrame.setVisible(True)
    
    def on_impotToLayer_toggled(self):
        self.dbFrame.setVisible(False)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def on_selectDirectoryWidget_fileChanged(self):
        if self.selectDirectoryWidget.filePath():
            self.analizeButton.setEnabled(True)
            self.importButton.setEnabled(True)
        else:
            self.analizeButton.setEnabled(False)
            self.importButton.setEnabled(False)
