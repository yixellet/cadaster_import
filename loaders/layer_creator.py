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
                  'ascendant_cad_numbers', 'descendant_cad_numbers', 'included_objects', 'facility_cad_number', 'common_land']
    }
    def __init__(self):
        pass
    
    @classmethod
    def createLandsLayer(self):
        vl = QgsVectorLayer('MultiPolygon', 'temp_lands', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS['land']:
                pr.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vl.updateFields()
        QgsProject.instance().addMapLayer(vl)
        return vl
    
    @classmethod
    def createConstructionsPolygonLayer(self):
        vl = QgsVectorLayer('MultiPolygon', 'temp_constructions__polygon', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS['construction']:
                pr.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vl.updateFields()
        QgsProject.instance().addMapLayer(vl)
        return vl
    
    @classmethod
    def createConstructionsLineLayer(self):
        vl = QgsVectorLayer('LineString', 'temp_constructions__line', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            if field['name'] in self.FIELDS['construction']:
                pr.addAttributes([QgsField(name=field['name'], type=field['type'], comment=field['desc'])])
        vl.updateFields()
        QgsProject.instance().addMapLayer(vl)
        return vl

    @classmethod
    def loadData(self, layer, data, type):
        feat = QgsFeature(layer.fields())
        if data['geom'] != None:
            feat.setGeometry(QgsGeometry.fromWkt(data['geom']))
        for field in self.FIELDS[type]:
            '''
            if type == 'construction':
                logMessage(field + '\t' + str(data[field]))
            '''
            feat.setAttribute(field, str(data[field]) if isinstance(data[field], (dict, list)) else data[field])
        layer.dataProvider().addFeature(feat)
        layer.updateExtents()
