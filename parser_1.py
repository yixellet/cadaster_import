import xml.etree.ElementTree as ET
import re
from .parser_elements.details_statement import detailsStatement
from .parser_elements.parse_eapl import parseEapl
from .parser_elements.parse_eapc import parseEapc
from .parser_elements.quarter import quarter
from .parser_elements.land_records import land_records
from .parser_elements.mun_boundaries import mun_boundaries
from .parser_elements.contours import getGeometryInfo
from .loaders.layer_creator import LayerCreator
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

    def getFileType(self):
        print(self.root.tag)
        return {'tag': self.root.tag, 'name': self.FILE_TYPES[self.root.tag]['name']}
    
    def parse(self):
        result = {}
        result.update(detailsStatement(self.root))
        if self.root.tag == 'extract_about_property_land':
            result.update(parseEapl(self.root))
            LayerCreator.loadData(result)
        if self.root.tag == 'extract_about_property_construction':
            result.update(parseEapc(self.root))
            LayerCreator.loadData(result)
        if self.root.tag == 'extract_cadastral_plan_territory':
            #logMessage(self.root.tag)
            result.update(quarter(self.root))
            LayerCreator.loadData(result)
            lands = land_records(self.root)
            for land_record in lands:
                land_record.update(detailsStatement(self.root))
                LayerCreator.loadData(land_record)
            mun_bounds = mun_boundaries(self.root)
            for mun_bound in mun_bounds:
                LayerCreator.loadData(mun_bound)
    
    def extractGeometryInfo(self):
        if self.root.tag == 'extract_about_property_construction':
            if self.root.find('construction_record').find('contours'):
                return getGeometryInfo(self.root.find('construction_record').find('contours'))
        if self.root.tag == 'extract_about_property_land':
            if self.root.find('land_record').find('contours_location'):
                return getGeometryInfo(self.root.find('land_record').find('contours_location').find('contours'))
        if self.root.tag == 'extract_about_boundary':
            if self.root.find('boundary_record').find('subject_boundary'):
                if self.root.find('boundary_record').find('subject_boundary').find('contours_location'):
                    return getGeometryInfo(self.root.find('boundary_record').find('subject_boundary').find('contours_location').find('contours'))
            if self.root.find('boundary_record').find('municipal_boundary'):
                if self.root.find('boundary_record').find('municipal_boundary').find('contours_location'):
                    return getGeometryInfo(self.root.find('boundary_record').find('municipal_boundary').find('contours_location').find('contours'))
            if self.root.find('boundary_record').find('inhabited_locality_boundary'):
                if self.root.find('boundary_record').find('inhabited_locality_boundary').find('contours_location'):
                    return getGeometryInfo(self.root.find('boundary_record').find('inhabited_locality_boundary').find('contours_location').find('contours'))
        if self.root.tag == 'extract_about_zone':
            if self.root.find('zone_territory_coastline_surveying').find('zones_and_territories'):
                if self.root.find('zone_territory_coastline_surveying').find('zones_and_territories').find('contours_location'):
                    return getGeometryInfo(self.root.find('zone_territory_coastline_surveying').find('zones_and_territories').find('contours_location').find('contours'))
            if self.root.find('zone_territory_coastline_surveying').find('coastline'):
                if self.root.find('zone_territory_coastline_surveying').find('coastline').find('contours_location'):
                    return getGeometryInfo(self.root.find('zone_territory_coastline_surveying').find('coastline').find('contours_location').find('contours'))
            if self.root.find('zone_territory_coastline_surveying').find('surveying_project'):
                if self.root.find('zone_territory_coastline_surveying').find('surveying_project').find('contours_location'):
                    return getGeometryInfo(self.root.find('zone_territory_coastline_surveying').find('surveying_project').find('contours_location').find('contours'))
        return None
