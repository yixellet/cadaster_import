import xml.etree.ElementTree as ET
from datetime import date
import re
from .parser_elements.details_statement import detailsStatement
from .parser_elements.parse_eapl import parseEapl
from .parser_elements.parse_eapc import parseEapc
from .parser_elements.common_data import commonData
from .parser_elements.quarter import quarter
# from .parser_elements.land_records import land_records
from .parser_elements.LandRecord import LandRecord
from .parser_elements.mun_boundaries import mun_boundaries
from .parser_elements.zones import zones
from .parser_elements.coastlines import coastlines
from .parser_elements.contours import getGeometryInfo
from .loaders.layer_creator_1 import LayerCreator
from .cadaster_import_utils import logMessage

class Parser():
    
    FILE_TYPES = {
        'extract_about_property_land': {
            'name': 'Кадастровая выписка о земельном участке'
        },
        'extract_about_property_construction': {
            'name': 'Кадастровая выписка об объекте капитального строительства'
        },
        'extract_about_boundary': {
            'name': 'Кадастровая выписка об административной границе'
        },
        'extract_about_property_build': {
            'name': 'Кадастровая выписка о здании'
        },
        'extract_about_property_property_complex': {
            'name': 'Кадастровая выписка о предприятии как имущественном комплексе'
        },
        'extract_about_property_room': {
            'name': 'Кадастровая выписка о помещении'
        },
        'extract_about_property_under_construction': {
            'name': 'Кадастровая выписка об объекте незавершенного строительства'
        },
        'extract_about_property_unified_real_estate_complex': {
            'name': 'Кадастровая выписка о едином недвижимом комплексе'
        },
        'extract_about_zone': {
            'name': 'Выписка о зоне с особыми условиями использования территорий'
        },
        'extract_cadastral_plan_territory': {
            'name': 'Кадастровый план территории'
        }
    }

    def __init__(self, xml):
        self.tree = ET.parse(xml)
        self.root = self.tree.getroot()
    
    def getFileType(self) -> dict[str, str, str, date]:
        """
        Выполняет первичную проверку XML документа по корневому тегу,
        является ли он выпиской из ЕГРН.
        Если корневой тег документа соответствует одному из тегов,
        перечисленных в константе FILE_TYPES, функция генерирует словарь
        следующего формата:
        {
            'tag': <корневой тег>,
            'name': <тип документа (на русском языке)>,
            'cadastral_number': <кадастровый (регистрационный) номер
                объекта, описанного в документе>,
            'date_formation': <дата формирования настоящего документа>
        }
        """
        result = None
        if self.root.tag in self.FILE_TYPES.keys():
            result = {'tag': self.root.tag, 
                      'name': self.FILE_TYPES[self.root.tag]['name'],
                      'date_formation': date.fromisoformat(detailsStatement(self.root)['date_formation'])}
            if self.root.tag == 'extract_cadastral_plan_territory':
                result.update({
                    'cadastral_number': quarter(self.root)['cadastral_number']})
            elif self.root.tag == 'extract_about_property_land':
                object = self.root.find('land_record').find('object')
                result.update({
                    'cadastral_number': commonData(object)['cad_number']})
        return result
    
    def parse(self):
        result = {}
        details = detailsStatement(self.root)
        result.update(details)
        if self.root.tag == 'extract_about_property_land':
            result.update(parseEapl(self.root))
            LayerCreator.loadData(result)
        if self.root.tag == 'extract_about_property_construction':
            result.update(parseEapc(self.root))
            LayerCreator.loadData(result)
        if self.root.tag == 'extract_cadastral_plan_territory':
            cad_blocks = self.root.find('cadastral_blocks')
            if cad_blocks:
                for block in cad_blocks.findall('cadastral_block'):
                    record_data = block.find('record_data')
                    if record_data:
                        base_data = record_data.find('base_data')
                        land_records = base_data.find('land_records')
                        if land_records:
                            for land_record in land_records:
                                record= LandRecord(land_record)
                                record.parse()
                                data = record.data
                                data.update(details)
                                LayerCreator.loadData(data)
            """
            result.update(quarter(self.root))
            LayerCreator.loadData(result)
            lands = land_records(self.root)
            if lands:
                for land_record in lands:
                    land_record.update(detailsStatement(self.root))
                    LayerCreator.loadData(land_record)
            
            mun_bounds = mun_boundaries(self.root)
            if mun_bounds:
                for mun_bound in mun_bounds:
                    LayerCreator.loadData(mun_bound)
            coastline = coastlines(self.root)
            if coastline:
                for c in coastline:
                    LayerCreator.loadData(c)

            
            zone = zones(self.root)
            if zone:
                for z in zone:
                    LayerCreator.loadData(z)
            """