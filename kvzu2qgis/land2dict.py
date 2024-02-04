import xml.etree.ElementTree as ET
import re
from transform import transform

def parseXML(xmlfile):
    land = {}
    tree = ET.parse(xmlfile)
    root = tree.getroot()


    # --- СВЕДЕНИЯ О КАДАСТРОВОЙ ВЫПИСКЕ ---
    ds = root.find('details_statement')

    # "Высшие реквизиты" - номер и дата выписки
    gtr = ds.find('group_top_requisites')
    if gtr.find('registration_number') != None:
        land['extract_number'] = gtr.find('registration_number').text
    else:
        land['extract_number'] = None
    land['extract_date'] = gtr.find('date_formation').text

    # "Низшие реквизиты" - должность и имя регистратора
    if ds.find('group_lower_requisites') != None:
        land['position'] = ds.find('group_lower_requisites').find('full_name_position').text
        land['name'] = ds.find('group_lower_requisites').find('initials_surname').text
    else:
        land['position'] = None
        land['name'] = None
    
    
    # --- СВЕДЕНИЯ О ЗЕМЕЛЬНОМ УЧАСТКЕ ---
    lr = root.find('land_record')
    
    # Даты регистрации и снятия с учета
    ri = lr.find('record_info')
    land['reg_date'] = ri.find('registration_date').text
    if ri.find('cancel_date') != None:
        land['cancel_date'] = ri.find('cancel_date').text
    else:
        land['cancel_date'] = None

    # Общие сведения (кадастровый номер и тип)
    ol = lr.find('object')
    land['cad_number'] = ol.find('common_data').find('cad_number').text
    type = {}
    type['code'] = ol.find('common_data').find('type').find('code').text
    type['value'] = ol.find('common_data').find('type').find('value').text
    land['type'] = type
    subtype = {}
    subtype['code'] = ol.find('subtype').find('code').text
    subtype['value'] = ol.find('subtype').find('value').text
    land['subtype'] = subtype

    # Дата постановки на учет по документу
    if ol.find('reg_date_by_doc') != None:
        land['reg_date_by_doc'] = ol.find('reg_date_by_doc').text
    else:
        land['reg_date_by_doc'] = None
    
    # Связь с кадастровыми номерами
    if lr.find('cad_links') != None:
        cl = lr.find('cad_links')

        # Недвижимость на участке
        if cl.find('included_objects') != None:
            io = cl.find('included_objects')
            ios = []
            for e in io.findall('included_object'):
                cn = e.find('cad_number').text
                cns = re.split('[,;]\s*', cn)
                ios = ios + cns
            land['included_objects'] = ios
        else:
            land['included_objects'] = None
        
        # Участки, из которых образован данный
        if cl.find('ascendant_cad_numbers') != None:
            io = cl.find('ascendant_cad_numbers')
            ios = []
            for e in io.findall('ascendant_cad_number'):
                cn = e.find('cad_number').text
                cns = re.split('[,;]\s*', cn)
                ios = ios + cns
            land['ascendant_cad_numbers'] = ios
        else:
            land['ascendant_cad_numbers'] = None
        
        # Участки, образованные из данного
        if cl.find('descendant_cad_numbers') != None:
            io = cl.find('descendant_cad_numbers')
            ios = []
            for e in io.findall('descendant_cad_number'):
                cn = e.find('cad_number').text
                cns = re.split('[,;]\s*', cn)
                ios = ios + cns
            land['descendant_cad_numbers'] = ios
        else:
            land['descendant_cad_numbers'] = None
        
        # Предприятие, в состав которого входит данный ЗУ
        if cl.find('facility_cad_number') != None:
            land['facility_cad_number'] = cl.find('facility_cad_number').text
        else:
            land['facility_cad_number'] = None
        
        # Единое землепользование
        if cl.find('common_land') != None:
            numbers = cl.find('common_land').find('common_land_parts').find('included_cad_numbers')
            ios = []
            for e in numbers.findall('included_cad_number'):
                cn = e.find('cad_number').text
                cns = re.split('[,;]\s*', cn)
                ios = ios + cns
            land['common_land_cad_numbers'] = ios            
        else:
            land['common_land_cad_numbers'] = None
        
        # Ранее присвоенные номера
        if cl.find('old_numbers') != None:
            ons = []
            for e in cl.find('old_numbers').findall('old_number'):
                on = {}
                on['number'] = e.find('number').text
                if e.find('assignment_date') != None:
                    on['assignment_date'] = e.find('assignment_date').text
                else:
                    on['assignment_date'] = None
                if e.find('assigner') != None:
                    on['assigner'] = e.find('assigner').text
                else:
                    on['assigner'] = None
                on['type'] = {'code': e.find('number_type').find('code').text, 'value': e.find('number_type').find('value').text}
        else:
            land['old_numbers'] = None


    # Характеристики земельного участка
    p = lr.find('params')
    c = p.find('category')
    land['category'] = {'code': c.find('type').find('code').text, 'value': c.find('type').find('value').text}
    a = p.find('area')
    land['area'] = {'value': a.find('value').text}
    
    if a.find('inaccuracy') != None:
        land['area']['inaccuracy'] = a.find('inaccuracy').text
    else:
        land['area']['inaccuracy'] = None
    
    if a.find('type') != None:
        land['area']['type'] = {'code': a.find('type').find('code').text, 'value': a.find('type').find('value').text}
    else:
        land['area']['type'] = None

    if p.find('permitted_use') != None:
        pue = p.find('permitted_use').find('permitted_use_established')
        obj = {}
        if pue.find('by_document') != None:
            obj['by_document'] = pue.find('by_document').text
        else:
            obj['by_document'] = None
        if pue.find('land_use') != None:
            obj['land_use'] = {'code': pue.find('land_use').find('code').text, 'value': pue.find('land_use').find('value').text}
        else:
            obj['land_use'] = {'code': None, 'value': None}
        if pue.find('land_use_mer') != None:
            obj['land_use_mer'] = {'code': pue.find('land_use_mer').find('code').text, 'value': pue.find('land_use_mer').find('value').text}
        else:
            obj['land_use_mer'] = {'code': None, 'value': None}
        
        land['permitted_use'] = obj
    else:
        land['permitted_use'] = None

    if p.find('permittes_uses_grad_reg') != None:
        pugr = p.find('permittes_uses_grad_reg')
        obj = {}
        if pugr.find('reg_numb_border') != None:
            obj['reg_numb_border'] = pugr.find('reg_numb_border').text
        else:
            obj['reg_numb_border'] = None
        if pugr.find('land_use') != None:
            obj['land_use'] = {'code': pugr.find('land_use').find('code').text, 'value': pugr.find('land_use').find('value').text}
        else:
            obj['land_use'] = {'code': None, 'value': None}
        if pugr.find('permitted_use_text') != None:
            obj['permitted_use_text'] = pugr.find('permitted_use_text').text
        else:
            obj['permitted_use_text'] = None

        land['permittes_uses_grad_reg'] = obj
    else:
        land['permitted_use_grad_reg'] = None


    # Адрес
    if lr.find('address_location') != None:
        a = lr.find('address_location')
        obj = {}
        if a.find('address_type') != None:
            obj['address_type'] = {'code': a.find('address_type').find('code').text, 'value': a.find('address_type').find('value').text}
        else:
            obj['address_type'] = {'code': None, 'value': None}
        
        addr = a.find('address')
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
            afobj['region'] = {'code': ls.find('region').find('code').text, 'value': ls.find('region').find('value').text}
            if ls.find('district') != None:
                afobj['district'] = {'type': ls.find('district').find('type_district').text, 'name': ls.find('district').find('name_district').text}
            else:
                afobj['district'] = None
            if ls.find('city') != None:
                afobj['city'] = {'type': ls.find('city').find('type_city').text, 'name': ls.find('city').find('name_city').text}
            else:
                afobj['city'] = None
            if ls.find('urban_district') != None:
                afobj['urban_district'] = {'type': ls.find('urban_district').find('type_urban_district').text, 'name': ls.find('urban_district').find('name_urban_district').text}
            else:
                afobj['urban_district'] = None
            if ls.find('soviet_village') != None:
                afobj['soviet_village'] = {'type': ls.find('soviet_village').find('type_soviet_village').text, 'name': ls.find('soviet_village').find('name_soviet_village').text}
            else:
                afobj['soviet_village'] = None
            if ls.find('locality') != None:
                afobj['locality'] = {'type': ls.find('locality').find('type_locality').text, 'name': ls.find('locality').find('name_locality').text}
            else:
                afobj['locality'] = None
            
            dl = af.find('detailed_level')
            if dl.find('street') != None:
                afobj['street'] = {'type': dl.find('street').find('type_street').text, 'name': dl.find('street').find('name_street').text}
            else:
                afobj['street'] = None
            if dl.find('Level1') != None:
                afobj['Level1'] = {'type': dl.find('Level1').find('type_Level1').text, 'name': dl.find('Level1').find('name_Level1').text}
            else:
                afobj['Level1'] = None
            if dl.find('Level2') != None:
                afobj['Level2'] = {'type': dl.find('Level2').find('type_Level2').text, 'name': dl.find('Level2').find('name_Level2').text}
            else:
                afobj['Level2'] = None
            if dl.find('Level3') != None:
                afobj['Level3'] = {'type': dl.find('Level3').find('type_Level3').text, 'name': dl.find('Level3').find('name_Level3').text}
            else:
                afobj['Level3'] = None
            if dl.find('apartment') != None:
                afobj['apartment'] = {'type': dl.find('apartment').find('type_apartment').text, 'name': dl.find('apartment').find('name_apartment').text}
            else:
                afobj['apartment'] = None
            if dl.find('other') != None:
                afobj['other'] = dl.find('other').text
            else:
                afobj['other'] = None

            ad['address_fias'] = afobj
        else:
            ad['address_fias'] = None

        obj['address'] = ad

        if a.find('rel_position') != None:
            rp = a.find('rel_position')
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
            obj['rel_position'] = objj
        else:
            obj['rel_position'] = None

        land['address_location'] = obj
    else:
        land['address_location'] = None

    # Кадастровый инженер
    if lr.find('cad_works') != None:
        cw = []
        for w in lr.find('cad_works').findall('cad_work'):
            work = {}
            if w.find('work_type') != None:
                work['work_type'] = w.find('work_type').text
            else:
                work['work_type'] = None
            if w.find('cadastral_engineer_agreement') != None:
                work['cadastral_engineer_agreement'] = w.find('cadastral_engineer_agreement').text
            else:
                work['cadastral_engineer_agreement'] = None
            if w.find('cadastral_engineer_registry_number') != None:
                work['cadastral_engineer_registry_number'] = w.find('cadastral_engineer_registry_number').text
            else:
                work['cadastral_engineer_registry_number'] = None
            if w.find('cadastral_engineer_date') != None:
                work['cadastral_engineer_date'] = w.find('cadastral_engineer_date').text
            else:
                work['cadastral_engineer_date'] = None
            work['fio'] = w.find('fio_cad_ingineer').find('surname').text + ' ' + w.find('fio_cad_ingineer').find('name').text
            if w.find('fio_cad_ingineer').find('patronymic') != None:
                work['fio'] += ' ' + w.find('fio_cad_ingineer').find('patronymic').text
            cw.append(work)
        land['cad_works'] = cw
        
    else:
        land['cad_works'] = None


    # Зоны и территории
    if lr.find('zones_and_boundaries') != None:
        zb = lr.find('zones_and_boundaries')
        if zb.find('special_economic_boundary') != None:
            sebs = []
            for b in zb.find('special_economic_boundary').findall('special_economic_boundaries'):
                sebs.append(b.find('reg_numb_border').text)
            land['special_economic_boundary'] = sebs
        else:
            land['special_economic_boundary'] = None

        if zb.find('special_use_boundaries') != None:
            sebs = []
            for b in zb.find('special_use_boundaries').findall('special_use_boundary'):
                sebs.append(b.find('reg_numb_border').text)
            land['special_use_boundaries'] = sebs
        else:
            land['special_use_boundaries'] = None

        if zb.find('guarded_natural_boundaries') != None:
            sebs = []
            for b in zb.find('guarded_natural_boundaries').findall('guarded_natural_boundary'):
                sebs.append(b.find('reg_numb_border').text)
            land['guarded_natural_boundaries'] = sebs
        else:
            land['guarded_natural_boundaries'] = None


    # Части ЗУ
    if lr.find('object_parts') != None:
        for p in lr.find('object_parts').findall('object_part'):
            pass



    # Описание местоположения границ ЗУ
    if lr.find('contours_location') != None:
        contAr = []
        for p in lr.find('contours_location').find('contours').findall('contour'):
            esArr = []
            es = p.find('entity_spatial')
            for e in es.find('spatials_elements').findall('spatial_element'):
                elAr = []
                for o in e.find('ordinates').findall('ordinate'):
                    coords = transform([float(o.find('x').text), float(o.find('y').text)], 2)
                    elAr.append(' '.join([str(coords[1]), str(coords[0])]))
                elementWKT = '(' + ','.join(elAr) + ')'
                esArr.append(elementWKT)
            contourWKT = '(' + ','.join(esArr) + ')'
            contAr.append(contourWKT)
        geomWKT = 'MULTIPOLYGON(' + ','.join(contAr) + ')'
        land['geom'] = geomWKT
        
            






    # Особые отметки
    if lr.find('special_notes') != None:
        land['special_notes'] = lr.find('special_notes').text
    else:
        land['special_notes'] = None



    # --- СВЕДЕНИЯ О ПРАВАХ ---
    if root.find('right_records') != None:
        rr = root.find('right_records')
        for rec in rr.findall('right_record'):
            pass


    # --- ОГРАНИЧЕНИЯ И ОБРЕМЕНЕНИЯ ---
    if root.find('restrict_records') != None:
        rr = root.find('restrict_records')
        for rec in rr.findall('restrict_record'):
            pass


    # --- БЕСХОЗЯЙНОЕ ИМУЩЕСТВО ---
    if root.find('ownerless_right_record') != None:
        pass


    # --- СВЕДЕНИЯ О ПРАВОПРИТЯЗАНИЯХ ---
    if root.find('claim_records') != None:
        rr = root.find('claim_records')
        for rec in rr.findall('claim_record'):
            pass


    # --- СВЕДЕНИЯ О СДЕЛКАХ ---
    if root.find('deal_records') != None:
        rr = root.find('deal_records')
        for rec in rr.findall('deal_record'):
            pass


    # --- СВЕДЕНИЯ О НЕВОЗМОЖНОСТИ РЕГИСТРАЦИИ ---
    if root.find('non_registrabilitys') != None:
        rr = root.find('non_registrabilitys')
        for rec in rr.findall('non_registrability'):
            pass
    
    return land

if __name__ == '__main__':
    import pprint
    from insert_into_table import insertIntoTable
    from connection import connectToDB
    from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_SCHEMA, DB_TABLE

    (connection, cursor) = connectToDB(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)

    pp = pprint.PrettyPrinter(indent=2)
    with open('data/30_04_000000_201/report-bf2fc54e-89e3-41ee-9ae6-4b9b0d77b09c-OfSite-2023-10-12-659795-30-01[0].xml', encoding="utf8") as f:
        data = parseXML(f)
        insertIntoTable(cursor, connection, DB_SCHEMA, DB_TABLE, data)
        #parseXML(f)
    #with open('test.xml', encoding="utf8") as f:
        #print(parseXML(f))