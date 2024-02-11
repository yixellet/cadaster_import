import xml.etree.ElementTree as ET

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

    def __init__(self):
        pass

    @classmethod
    def getFileType(self, xml):
        tree = ET.parse(xml)
        root = tree.getroot()
        self.result = {'type': root.tag, 'name': self.FILE_TYPES[root.tag]['name']}
        #logMessage(str(result))
        return self.result
    
    @classmethod
    def parse(self, xml):
        from .parser_elements.details_statement import detailsStatement
        from .parser_elements.parse_eapl import parseEapl
        from .loaders.layer_creator import LayerCreator
        tree = ET.parse(xml)
        root = tree.getroot()
        result = {}
        result.update(detailsStatement(root))
        if root.tag == 'extract_about_property_land':
            result.update(parseEapl(root))
            l = LayerCreator.createLandsLayer()
            LayerCreator.loadData(l, result)
        #logMessage(str(result))