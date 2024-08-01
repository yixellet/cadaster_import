from .Geometry import Geometry
from ..cadaster_import_utils import logMessage

def zones(root):
    """
    Извлекает инфо о границах зон из КПТ
    """
    OBJECT_TYPE = 'zones'
    cadastral_blocks = root.find('cadastral_blocks')
    cadastral_block = cadastral_blocks.find('cadastral_block')

    if cadastral_block.find('zones_and_territories_boundaries') != None:
        result = []
        for boundary in cadastral_block.find('zones_and_territories_boundaries').findall('zones_and_territories_record'):
            record = {}
            record['quartal'] = cadastral_block.find('cadastral_number').text
            b_object_zones_and_territories = boundary.find('b_object_zones_and_territories')
            b_object = b_object_zones_and_territories.find('b_object')
            record['registration_number'] = b_object.find('reg_numb_border').text
            record['registration_date'] = boundary.find('record_info').find('registration_date').text
            record['type_boundary'] = b_object.find('type_boundary').find('value').text
            if b_object_zones_and_territories.find('type_zone') != None and b_object_zones_and_territories.find('type_zone').find('value') != None:
                record['type_zone'] = b_object_zones_and_territories.find('type_zone').find('value').text
            else:
                record['type_zone'] = None

            record['content'] = OBJECT_TYPE
            geometry = Geometry(boundary.find('b_contours_location'), OBJECT_TYPE, record['registration_number'])
            geometry_array = geometry.extract_geometry()
            
            for contour in geometry_array:
                contour.update(record)
                result.append(contour)
    else:
        result = None

    return result
