from .cad_work import cadWork
from .address import address
from .record_info import recordInfo
from .common_data import commonData
from .land_params import landParams
from .cad_link import cadLink
from .contours import contours, getMskZone

def parseEapl(root):
    '''
    Парсит КВЗУ
    '''
    result = {}
    lr = root.find('land_record')

    result['content'] = 'land'

    # Даты государственной регистрации
    result.update(recordInfo(lr.find('record_info')))

    object = lr.find('object')
    # Кадастровый номер и вид объекта недвижимости
    result.update(commonData(object))

    # Параметры участка
    result.update(landParams(lr))

    # Сведения о кадастровом инженере
    if lr.find('cad_works') != None:
        cad_works = []
        for work in lr.find('cad_works').findall('cad_work'):
            w = cadWork(work)
            cad_works.append(w)
        result['cad_works'] = cad_works
    else:
        result['cad_works'] = None

    # Связь с кадастровыми номерами
    if lr.find('cad_links') != None:
        result['ascendant_cad_numbers'] = cadLink(lr.find('cad_links'), 'ascendant_cad_numbers')
        result['descendant_cad_numbers'] = cadLink(lr.find('cad_links'), 'descendant_cad_numbers')
        result['included_objects'] = cadLink(lr.find('cad_links'), 'included_objects')
        result['facility_cad_number'] = cadLink(lr.find('cad_links'), 'facility_cad_number')
        #result['old_numbers'] = cadLink(lr.find('cad_links'), 'old_numbers')
        if lr.find('cad_links').find('common_land') != None:
            result['common_land'] = cadLink(lr.find('cad_links').find('common_land').find('common_land_parts'), 'included_cad_numbers')
        else:
            result['common_land'] = None
    else:
        result['ascendant_cad_numbers'] = None
        result['descendant_cad_numbers'] = None
        result['included_objects'] = None
        result['facility_cad_number'] = None
        #result['old_numbers'] = None
        result['common_land'] = None

    # Сведения об адресном ориентире
    if lr.find('address_location') != None:
        result.update(address(lr.find('address_location')))
    else:
        result['address_type'] = None
        result['address'] = None
        result['rel_position'] = None

    # Описание местоположения границ ЗУ
    if lr.find('contours_location') != None:
        result['geom'] = contours(lr.find('contours_location').find('contours'))['geom']
        result['msk_zone'] = contours(lr.find('contours_location').find('contours'))['msk_zone']
        #result['msk_zone'] = getMskZone(lr.find('contours_location').find('contours').find('contour').find('entity_spatial'))
    else:
        result['geom'] = None
    
    result['content'] = 'lands'
    result['geometryType'] = 'MultiPolygon'

    return result