from qgis.core import QgsMessageLog, Qgis

def logMessage(message, level=Qgis.Info):
    QgsMessageLog.logMessage(message, 'XML Import', level)