from .common_data import commonData
from .land_params import landParams
from .address import address
from .contours import contours, extract_zone_contours_2
from ..cadaster_import_utils import logMessage

def land_records(root):
    """
    Извлекает инфо о земельных участках из КПТ
    """
    result = None
    if root.find('cadastral_blocks').find('cadastral_block').find('record_data') != None:
        if root.find('cadastral_blocks').find('cadastral_block').find('record_data').find('base_data').find('land_records') != None:
            result = []
            land_records = root.find('cadastral_blocks').find('cadastral_block').find('record_data').find('base_data').find('land_records')
            for land_record in land_records.findall('land_record'):
                record = {}
                record.update(commonData(land_record.find('object')))
                #logMessage(record['cad_number'])
                record.update(landParams(land_record))
                if land_record.find('address_location') != None:
                    record.update(address(land_record.find('address_location')))
                else:
                    record['address'] = None
                    record['address_type'] = None
                if land_record.find('contours_location') != None:
                    # logMessage(land_record.find('contours_location').text)
                    contours = extract_zone_contours_2(land_record.find('contours_location'))[0]
                    #logMessage(str(contours))
                    record.update(contours)
                else:
                    record['geom'] = None
                    if record['cad_number'][3:4] in ('01', '03', '07', '08', '10', '11'):
                        record['msk_zone'] = '1'
                    else:
                        record['msk_zone'] = '2'
                if record['msk_zone'] == None:
                    if record['cad_number'][3:4] in ('01', '03', '07', '08', '10', '11'):
                        record['msk_zone'] = '1'
                    else:
                        record['msk_zone'] = '2'
                    
                record['content'] = 'lands'
                record['geometryType'] = 'MultiPolygon'
                result.append(record)

    return result