import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    land = {}
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    gtr = root.find('details_statement').find('group_top_requisites')
    land['extract_number'] = gtr.find('registration_number').text
    land['extract_date'] = gtr.find('date_formation').text

    lr = root.find('land_record')
    land['reg_date'] = lr.find('record_info').find('registration_date').text
    land['cad_number'] = lr.find('object').find('common_data').find('cad_number').text
    type = {}
    type['code'] = lr.find('object').find('common_data').find('type').find('code').text
    type['value'] = lr.find('object').find('common_data').find('type').find('value').text
    land['type'] = type
    subtype = {}
    subtype['code'] = lr.find('object').find('subtype').find('code').text
    subtype['value'] = lr.find('object').find('subtype').find('value').text
    land['subtype'] = subtype

    cl = lr.find('cad_links')
    io = cl.find('included_objects')
    ios = []
    for e in io.findall('included_object'):
        ios.append(e.find('cad_number').text)
    land['included_objects'] = ios
    """
    cad_blocks = root.find('cadastral_blocks')
    cad_block = cad_blocks.find('cadastral_block')
    cad_quarter = {}
    cad_quarter['area'] = {'value': float(cad_block.find('area_quarter').find('area').text), 'unit': 'га'}
    lands = []
    record_data = cad_block.find('record_data')
    base_data = record_data.find('base_data')
    land_records = base_data.find('land_records')
    for e in land_records.findall('land_record'):
        land = {}
        object = e.find('object')
        common_data = object.find('common_data')
        type = common_data.find('type')
        land['type'] = type.find('value').text
        land['cadastral_number'] = common_data.find('cad_number').text
        print(common_data.find('cad_number').text)
        if object.find('subtype'):
            land['subtype'] = object.find('subtype').find('value').text
            if (object.find('subtype').find('code').text == '03' or object.find('subtype').find('code').text == '04') and e.find('cad_links'):
                cad_links = e.find('cad_links')
                com_land = cad_links.find('common_land')
                com_land_cn = com_land.find('common_land_cad_number')
                land['common_land_cad_num'] = com_land_cn.find('cad_number').text
            else:
                land['common_land_cad_num'] = None
        else:
            land['subtype'] = None
            land['common_land_cad_num'] = None
        params = e.find('params')
        if params.find('category'):
            land['category'] = params.find('category').find('type').find('value').text
        else:
            land['category'] = None
        if params.find('permitted_use'):
            pu = params.find('permitted_use')
            pue = pu.find('permitted_use_established')
            land['permitted_use'] = pue.find('by_document').text
        else:
            land['permitted_use'] = None
        if params.find('area'):
            a = params.find('area')
            land['area'] = float(a[0].text)
        else:
            land['area'] = None
        address = e.find('address_location').find('address')
        add_fias = address.find('address_fias').find('level_settlement')
        if add_fias.find('region'):
            land['region'] = add_fias.find('region').find('value').text
        else:
            land['region'] = None
        if add_fias.find('district'):
            land['district'] = add_fias.find('district').find('name_district').text + ' ' + add_fias.find('district').find('type_district').text
        else:
            land['district'] = None
        land['full_address'] = address.find('readable_address').text if address.find('readable_address') else None
        if e.find('cost'):
            land['cost'] = float(e.find('cost').find('value').text)
        else:
            land['cost'] = None
        if e.find('contours_location'):
            contours = e.find('contours_location').find('contours')
            conts = []
            for c in contours.findall('contour'):
                cont = []
                spatials_elements = c.find('entity_spatial').find('spatials_elements')
                for se in spatials_elements.findall('spatial_element'):
                    element = []
                    ordinates = se.find('ordinates')
                    for o in ordinates.findall('ordinate'):
                        element.append([float(o.find('x').text), float(o.find('y').text)])
                    cont.append(element)
                conts.append(cont)
            land['contours'] = conts
        else:
            land['contours'] = None
        lands.append(land)
    return lands
    """
    return land

if __name__ == '__main__':
    with open('./30_04_000000_201/report-bf2fc54e-89e3-41ee-9ae6-4b9b0d77b09c-OfSite-2023-10-12-659795-30-01[0].xml', encoding="utf8") as f:
        print(parseXML(f))