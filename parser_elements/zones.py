from .contours import contours

def zones(root):
    """
    Извлекает инфо о границах зон из КПТ
    """
    cadastral_blocks = root.find('cadastral_blocks')
    cadastral_block = cadastral_blocks.find('cadastral_block')

    if cadastral_block.find('zones_and_territories_boundaries') != None:
        result = []
        for boundary in cadastral_block.find('zones_and_territories_boundaries').findall('zones_and_territories_record'):
            record = {}
            b_object_zones_and_territories = boundary.find('b_object_zones_and_territories')
            b_object = b_object_zones_and_territories.find('b_object')
            record['registration_number'] = b_object.find('reg_numb_border').text
            record['registration_date'] = boundary.find('record_info').find('registration_date').text
            record['type_boundary'] = b_object.find('type_boundary').find('value').text
            if b_object_zones_and_territories.find('type_zone') != None and b_object_zones_and_territories.find('type_zone').find('value') != None:
                record['type_zone'] = b_object_zones_and_territories.find('type_zone').find('value').text
            else:
                record['type_zone'] = None
            record.update(contours(boundary.find('b_contours_location').find('contours')))

            record['content'] = 'zones'
            record['geometryType'] = 'MultiPolygon'
            result.append(record)


    return result
