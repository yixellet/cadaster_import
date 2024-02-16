from .dict import dict

def commonData(element):
    '''
    Извлекает кадастровый номер и тип объекта
    '''
    result = {}
    cd = element.find('common_data')
    result['cad_number'] = cd.find('cad_number').text
    result['type'] = dict(cd.find('type'))

    return result
