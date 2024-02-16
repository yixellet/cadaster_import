from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry

from .fields import fields
from ..cadaster_import_utils import logMessage

class LayerCreator():
    def __init__(self):
        pass
    
    @classmethod
    def createLandsLayer(self):
        vl = QgsVectorLayer('Polygon', 'temp_lands', 'memory')
        pr = vl.dataProvider()

        for field in fields.values():
            pr.addAttributes([QgsField(field['name'], field['type'])])
        vl.updateFields()

        return vl

    @classmethod
    def loadData(self, layer, data):
        #logMessage(data['cad_number'])
        feat = QgsFeature()
        if data['geom'] != None:
            feat.setGeometry(QgsGeometry.fromWkt(data['geom']))
        feat.setAttributes([
            data['extract_date'], 
            data['extract_number'], 
            None, None, None, 
            str(data['cad_works']), 
            data['address_type'], 
            str(data['address']), 
            str(data['rel_position']) if data['rel_position'] != None else data['rel_position'], 
            data['registration_date'], 
            data['cancel_date'], 
            data['cad_number'], 
            data['type'], 
            data['area'], 
            data['area_inaccuracy'], 
            data['area_type'], 
            data['land_use_by_document'], 
            data['land_use'], 
            data['land_use_mer'], 
            data['gr_reg_numb_border'], 
            data['gr_land_use'], 
            data['gr_permitted_use_text'], 
            str(data['ascendant_cad_numbers']) if data['ascendant_cad_numbers'] != None else data['ascendant_cad_numbers'], 
            str(data['descendant_cad_numbers']) if data['descendant_cad_numbers'] != None else data['descendant_cad_numbers'], 
            str(data['included_objects']) if data['included_objects'] != None else data['included_objects'], 
            str(data['facility_cad_number']) if data['facility_cad_number'] != None else data['facility_cad_number'], 
            str(data['old_numbers']) if data['old_numbers'] != None else data['old_numbers'], 
            str(data['common_land']) if data['common_land'] != None else data['common_land']])
        layer.dataProvider().addFeature(feat)
        layer.updateExtents()
