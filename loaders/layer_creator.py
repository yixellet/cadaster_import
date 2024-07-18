from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsProject

from .fields import fields
from ..cadaster_import_utils import logMessage

class LayerCreator():
    FIELDS = {
        'construction': ['registration_number', 'date_formation', 'address', 
                  'registration_date', 'cancel_date', 
                  'cad_number', 'land_cad_numbers', 'extension', 
                  'area', 'built_up_area', 'depth', 'occurence_depth', 
                  'volume', 'height', 'floors', 'underground_floors', 
                  'purpose', 'name', 'year_built', 'year_commisioning'],
        'land': ['registration_number', 'date_formation', 'cad_works', 'address', 
                  'registration_date', 'cancel_date', 'address_type', 'rel_position',
                  'cad_number', 'type', 'area_inaccuracy', 
                  'area', 'area_type', 'land_use_by_document', 'land_use', 
                  'land_use_mer', 'gr_reg_numb_border', 'gr_land_use', 'gr_permitted_use_text', 
                  'ascendant_cad_numbers', 'descendant_cad_numbers', 'included_objects', 'facility_cad_number', 'common_land'],
        'quarter': ['date_formation', 'cadastral_number', 'area']
    }
    def __init__(self):
        pass
    
    @classmethod
    def createLandsLayer(self):
        vl = QgsVectorLayer('MultiPolygon', 'temp_lands__', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS['land']:
                pr.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vl.updateFields()
        QgsProject.instance().addMapLayer(vl)
        return vl
    
    @classmethod
    def createConstructionsPolygonLayer(self):
        vl = QgsVectorLayer('MultiPolygon', 'temp_constructions__polygon__', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS['construction']:
                pr.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vl.updateFields()
        QgsProject.instance().addMapLayer(vl)
        return vl
    
    @classmethod
    def createConstructionsLineLayer(self):
        vl = QgsVectorLayer('LineString', 'temp_constructions__line__', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS['construction']:
                pr.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vl.updateFields()
        QgsProject.instance().addMapLayer(vl)
        return vl
    
    @classmethod
    def createQuartersLayer(self):
        vl = QgsVectorLayer('MultiPolygon', 'temp_quarters', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS['quarter']:
                pr.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vl.updateFields()
        QgsProject.instance().addMapLayer(vl)
        return vl
    
    @classmethod
    def createLayer(self, geometryType: str, content: str, mskZone: str):
        """Создаёт новый слой в QGIS и возвращает его.

        Аргументы:
        geometryType -- тип геометрии слоя (MultiPolygon или MultiLineString)
        content -- содержимое слоя (quarters, constructions, lands, zones, borders)
        mskZone -- зона МСК-30, в которой расположен объект (соответствует первой цифре координат Y объекта)
        """
        vectorLayer = QgsVectorLayer(geometryType, 'temp_' + content + '_' + geometryType + '__' + mskZone, 'memory')
        provider = vectorLayer.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS[content]:
                provider.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vectorLayer.updateFields()
        QgsProject.instance().addMapLayer(vectorLayer)
        return vectorLayer

    @classmethod
    def loadData(self, layer, data):
        feat = QgsFeature(layer.fields())
        if data['geom'] != None:
            feat.setGeometry(QgsGeometry.fromWkt(data['geom']))
        for field in self.FIELDS[data['content']]:
            feat.setAttribute(field, str(data[field]) if isinstance(data[field], (dict, list)) else data[field])
        
        
        
        layer.dataProvider().addFeature(feat)
        layer.updateExtents()
