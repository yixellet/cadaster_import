from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsProject
from qgis.PyQt.QtCore import QVariant

class LayerCreator():
    def __init__(self):
        pass
    
    @classmethod
    def createLandsLayer(self):
        vl = QgsVectorLayer('Polygon', 'temp_lands', 'memory')
        pr = vl.dataProvider()

        pr.addAttributes([QgsField('ext_numb', QVariant.String),
                          QgsField('ext_date', QVariant.String)])
        vl.updateFields()

        return vl

    @classmethod
    def loadData(self, layer, data):
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromWkt(data['geom']))
        feat.setAttributes([data['extract_number'], data['extract_date']])
        layer.dataProvider().addFeature(feat)
        layer.updateExtents()
        QgsProject.instance().addMapLayer(layer)
