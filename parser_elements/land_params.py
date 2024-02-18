from .dict import dict

def landParams(el):
    '''
    Извлекает Характеристики земельного участка
    '''

    land = {}
    element = el.find('params')
    # Категория разрешенного использования
    land['category'] = dict(element.find('category').find('type'))

    # Площадь
    a = element.find('area')
    land['area'] = int(a.find('value').text)
    
    if a.find('inaccuracy') != None:
        land['area_inaccuracy'] = float(a.find('inaccuracy').text)
    else:
        land['area_inaccuracy'] = None
    
    if a.find('type') != None:
        land['area_type'] = dict(a.find('type'))
    else:
        land['area_type'] = None

    # Вид разрешенного использования
    if element.find('permitted_use') != None:
        pue = element.find('permitted_use').find('permitted_use_established')
        if pue.find('by_document') != None:
            land['land_use_by_document'] = pue.find('by_document').text
        else:
            land['land_use_by_document'] = None
        if pue.find('land_use') != None:
            land['land_use'] = dict(pue.find('land_use'))
        else:
            land['land_use'] = None
        if pue.find('land_use_mer') != None:
            land['land_use_mer'] = dict(pue.find('land_use_mer'))
        else:
            land['land_use_mer'] = None
    else:
        land['land_use_by_document'] = None
        land['land_use'] = None
        land['land_use_mer'] = None

    # Вид разрешенного использования по градостроительному регламенту
    if element.find('permittes_uses_grad_reg') != None:
        pugr = element.find('permittes_uses_grad_reg')
        if pugr.find('reg_numb_border') != None:
            land['gr_reg_numb_border'] = pugr.find('reg_numb_border').text
        else:
            land['gr_reg_numb_border'] = None
        if pugr.find('land_use') != None:
            land['gr_land_use'] = dict(pugr.find('land_use'))
        else:
            land['gr_land_use'] = None
        if pugr.find('permitted_use_text') != None:
            land['gr_permitted_use_text'] = pugr.find('permitted_use_text').text
        else:
            land['gr_permitted_use_text'] = None
    else:
        land['gr_reg_numb_border'] = None
        land['gr_land_use'] = None
        land['gr_permitted_use_text'] = None


    return land
