from .common_data import commonData
from .land_params import landParams
from .address import address
from .contours import contours, extract_zone_contours_2
from Geometry import Geometry
from ..cadaster_import_utils import logMessage

def land_records(root):
    """
    Извлекает инфо о земельных участках из КПТ
    """
    OBJECT_TYPE = 'lands'
    result = None
    if root.find('cadastral_blocks').find('cadastral_block').find('record_data') != None:
        if root.find('cadastral_blocks').find('cadastral_block').find('record_data').find('base_data').find('land_records') != None:
            result = []
            land_records = root.find('cadastral_blocks').find('cadastral_block').find('record_data').find('base_data').find('land_records')
            for land_record in land_records.findall('land_record'):
                record = {}
                record['content'] = OBJECT_TYPE
                record.update(commonData(land_record.find('object')))
                record.update(landParams(land_record))
                
                if land_record.find('address_location') != None:
                    record.update(address(land_record.find('address_location')))
                else:
                    record['address'] = None
                    record['address_type'] = None
                
                contours_location = land_record.find('contours_location')
                
                if contours_location != None:
                    geometry = Geometry(contours_location, OBJECT_TYPE, record['cad_number'])
                    geometry_array = geometry.extract_geometry()

                    for contour in geometry_array:
                        contour.update(record)
                        result.append(contour)


                    contours = extract_zone_contours_2(land_record.find('contours_location'))[0]
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
                    
                record['geometryType'] = 'MultiPolygon'
                result.append(record)

    return result