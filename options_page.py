from qgis.gui import QgsOptionsPageWidget
from qgis.PyQt.QtWidgets import QHBoxLayout

class ConfigOptionsPage(QgsOptionsPageWidget):

    def __init__(self, parent):
        super().__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)