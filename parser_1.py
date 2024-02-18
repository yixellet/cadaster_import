import xml.etree.ElementTree as ET
from .parser_elements.details_statement import detailsStatement
from .parser_elements.parse_eapl import parseEapl
from .parser_elements.parse_eapc import parseEapc
from .cadaster_import_utils import logMessage

class Parser():
    
    FILE_TYPES = {
        'extract_about_property_land': {
            'name': 'Кадастровая выписка о земельном участке'
        },
        'extract_about_property_construction': {
            'name': 'Кадастровая выписка об объекте капитального строительства'
        },
        'extract_about_boundaries': {
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
        'extract_cadastral_plan_territory': {
            'name': 'Кадастровый план территории'
        }
    }

    def __init__(self, xml):
        self.tree = ET.parse(xml)
        self.root = self.tree.getroot()

    def getFileType(self):
        return self.root.tag
    
    def parse(self):
        result = {}
        result.update(detailsStatement(self.root))
        if self.root.tag == 'extract_about_property_land':
            result.update(parseEapl(self.root))
        if self.root.tag == 'extract_about_property_construction':
            result.update(parseEapc(self.root))

        return result