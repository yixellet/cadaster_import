from qgis.gui import QgsOptionsWidgetFactory
from PyQt5.QtGui import QIcon

from .options_page import ConfigOptionsPage

class OptionsFactory(QgsOptionsWidgetFactory):

    def __init__(self):
        super().__init__()

    def icon(self):
        return QIcon('icon.png')

    def createWidget(self, parent):
        return ConfigOptionsPage(parent)