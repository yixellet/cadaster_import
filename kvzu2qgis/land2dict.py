import xml.etree.ElementTree as ET
import re
from transform import transform

def parseXML(xmlfile):
    land = {}
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    
    # --- СВЕДЕНИЯ О ЗЕМЕЛЬНОМ УЧАСТКЕ ---
    lr = root.find('land_record')
    
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

    # Кадастровая стоимость
    if lr.find('cost') != None:
        land['cost'] = int(lr.find('cost').text)
    else:
        land['cost'] = None

    # Особые отметки
    if lr.find('special_notes') != None:
        land['special_notes'] = lr.find('special_notes').text
    else:
        land['special_notes'] = None



    # --- СВЕДЕНИЯ О ПРАВАХ ---
    if root.find('right_records') != None:
        rr = root.find('right_records')
        rights = []
        for rec in rr.findall('right_record'):
            right = {}
            right['date'] = rec.find('record_info').find('registration_date').text
            right['info'] = None
            rights.append(right)
        land['rights'] = rights
    else:
        land['rights'] = None


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