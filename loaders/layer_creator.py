from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsProject, QgsFeatureRequest

from .fields import fields
from ..cadaster_import_utils import logMessage

class LayerCreator():
    FIELDS = {
        'constructions': ['registration_number', 'date_formation', 'address', 
                  'registration_date', 'cancel_date', 
                  'cad_number', 'land_cad_numbers', 'extension', 
                  'area', 'built_up_area', 'depth', 'occurence_depth', 
                  'volume', 'height', 'floors', 'underground_floors', 
                  'purpose', 'name', 'year_built', 'year_commisioning'],
        #'lands': ['registration_number', 'date_formation', 'cad_works', 'address', 
        #          'registration_date', 'cancel_date', 'address_type', 'rel_position',
        #          'cad_number', 'type', 'area_inaccuracy', 
        #          'area', 'area_type', 'land_use_by_document', 'land_use', 
        #          'land_use_mer', 'gr_reg_numb_border', 'gr_land_use', 'gr_permitted_use_text', 
        #          'ascendant_cad_numbers', 'descendant_cad_numbers', 'included_objects', 'facility_cad_number', 'common_land'],
        'lands': ['registration_number', 'date_formation', 'address', 
                  'address_type', 
                  'cad_number', 'type', 'area_inaccuracy', 
                  'area', 'area_type', 'land_use_by_document', 'land_use', 
                  'land_use_mer'],
        'quarters': ['date_formation', 'cadastral_number', 'area'],
        'municipal_boundaries': ['registration_number', 'registration_number', 'type_boundary'],
        'zones': ['registration_number', 'registration_number', 'type_boundary', 'type_zone', 'quartal'],
        'coastlines': ['registration_number', 'registration_number', 'water']
    }
    def __init__(self):
        pass
    
    @classmethod
    def createLayer(self, geometryType: str, content: str, mskZone: str) -> QgsVectorLayer:
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
    def loadData(self, data: dict) -> None:
        """
        Создает новый (или берет существующий) слой и загружает в него объекты

        аргументы:
        data - словарь с распарсенным объектом
        """
        
        layers = { layer.name(): layer for layer in QgsProject.instance().mapLayers().values() }
        generatedLayerName = 'temp_' + data['content'] + '_' + data['geometryType'] + '__' + data['msk_zone']

        if generatedLayerName in layers.keys():
            layer = layers[generatedLayerName]
        else:
            layer = self.createLayer(data['geometryType'], data['content'], data['msk_zone'])
        
        s = None
        if data['content'] in ('municipal_boundaries', 'zones', 'coastlines'):
            s = layer.getFeatures(QgsFeatureRequest().setFilterExpression('"registration_number"=\'{}\''.format(data['registration_number'])))
        elif data['content'] in ('lands', 'constructions'):
            s = layer.getFeatures(QgsFeatureRequest().setFilterExpression('"cad_number"=\'{}\''.format(data['cad_number'])))
        elif data['content'] in ('quarters'):
            s = layer.getFeatures(QgsFeatureRequest().setFilterExpression('"cadastral_number"=\'{}\''.format(data['cadastral_number'])))
            # logMessage(str(s.isempty()))
        count = 0
        for f in s:
            count += 1

        if count == 0:
            feat = QgsFeature(layer.fields())
            # if data['content'] == 'zones':
                # logMessage(data['registration_number'] + ' ----> ' + data['geom'])
            if data['geom'] != None:
                if data['content'] in ('zones', 'lands'):
                    feat.setGeometry(data['geom'])
                else:
                    feat.setGeometry(QgsGeometry.fromWkt(data['geom']))
            
            for field in self.FIELDS[data['content']]:
                # logMessage(str(data))
                feat.setAttribute(field, str(data[field]) if isinstance(data[field], (dict, list)) else data[field])
            
            layer.dataProvider().addFeature(feat)
            layer.updateExtents()
