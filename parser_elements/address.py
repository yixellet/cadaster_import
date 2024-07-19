from .dict import dict

def getAddressPart(element, type):
    e = element.find(type)
    if e.find('type_{}'.format(type)):
        typeStr = e.find('type_{}'.format(type)).text
    else:
        typeStr = ''
    if e.find('name_{}'.format(type)):
        nameStr = e.find('name_{}'.format(type)).text
    else:
        nameStr = ''
    return typeStr + ' ' + nameStr

def address(element):
    '''
    Извлекает адрес
    '''    
    
    obj = {}

    # Тип адреса
    if element.find('address_type') != None:
        obj['address_type'] = dict(element.find('address_type'))
    else:
        obj['address_type'] = None
    
    # Адрес (местоположение)
    addr = element.find('address')
    ad = {}
    if addr.find('note') != None:
        ad['note'] = addr.find('note').text
    else:
        ad['note'] = None
    if addr.find('readable_address') != None:
        ad['readable_address'] = addr.find('readable_address').text
    else:
        ad['readable_address'] = None
    
    if addr.find('address_fias') != None:
        af = addr.find('address_fias')
        afobj = {}
        ls = af.find('level_settlement')
        if ls.find('fias') != None:
            afobj['objectid'] = ls.find('fias').text
        else:
            afobj['objectid'] = None
        if ls.find('okato') != None:
            afobj['okato'] = ls.find('okato').text
        else:
            afobj['okato'] = None
        if ls.find('kladr') != None:
            afobj['kladr'] = ls.find('kladr').text
        else:
            afobj['kladr'] = None
        if ls.find('oktmo') != None:
            afobj['oktmo'] = ls.find('oktmo').text
        else:
            afobj['oktmo'] = None
        if ls.find('postal_code') != None:
            afobj['postal_code'] = ls.find('postal_code').text
        else:
            afobj['postal_code'] = None
        if ls.find('region') != None:
            afobj['region'] = ls.find('region').text
        else:
            afobj['region'] = None
        if ls.find('district') != None:
            afobj['district'] = getAddressPart(ls, 'district')
        else:
            afobj['district'] = None
        if ls.find('city') != None:
            afobj['city'] = getAddressPart(ls, 'city')
        else:
            afobj['city'] = None
        if ls.find('urban_district') != None:
            afobj['urban_district'] = getAddressPart(ls, 'urban_district')
        else:
            afobj['urban_district'] = None
        if ls.find('soviet_village') != None:
            afobj['soviet_village'] = getAddressPart(ls, 'soviet_village')
        else:
            afobj['soviet_village'] = None
        if ls.find('locality') != None:
            afobj['locality'] = getAddressPart(ls, 'locality')
        else:
            afobj['locality'] = None
        
        if af.find('detailed_level') != None:
            dl = af.find('detailed_level')
            if dl.find('street') != None:
                afobj['street'] = getAddressPart(dl, 'street')
            else:
                afobj['street'] = None
            if dl.find('Level1') != None:
                afobj['Level1'] = getAddressPart(dl, 'Level1')
            else:
                afobj['Level1'] = None
            if dl.find('Level2') != None:
                afobj['Level2'] = getAddressPart(dl, 'Level2')
            else:
                afobj['Level2'] = None
            if dl.find('Level3') != None:
                afobj['Level3'] = getAddressPart(dl, 'Level3')
            else:
                afobj['Level3'] = None
            if dl.find('apartment') != None:
                afobj['apartment'] = getAddressPart(dl, 'apartment')
            else:
                afobj['apartment'] = None
            if dl.find('other') != None:
                afobj['other'] = dl.find('other').text
            else:
                afobj['other'] = None
        else:
            afobj['street'] = None
            afobj['Level1'] = None
            afobj['Level2'] = None
            afobj['Level3'] = None
            afobj['apartment'] = None
            afobj['other'] = None

        ad['address_fias'] = afobj
    else:
        ad['address_fias'] = None

    obj['address'] = str(ad)

    # Местоположение относительно ориентира
    if element.find('rel_position') != None:
        rp = element.find('rel_position')
        objj = {}
        if rp.find('in_boundaries_mark') != None:
            objj['in_boundaries_mark'] = rp.find('in_boundaries_mark').text
        else:
            objj['in_boundaries_mark'] = None
        if rp.find('ref_point_name') != None:
            objj['ref_point_name'] = rp.find('ref_point_name').text
        else:
            objj['ref_point_name'] = None
        if rp.find('location_description') != None:
            objj['location_description'] = rp.find('location_description').text
        else:
            objj['location_description'] = None
        obj['rel_position'] = str(objj)
    else:
        obj['rel_position'] = None

    return obj
