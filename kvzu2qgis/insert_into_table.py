from transform import transform

def insertIntoTable(cur, conn, data):
    for d in data:
        if d['contours']:
            cons = []
            for cont in d['contours']:
                els = []
                for el in cont:
                    c = []
                    for ordi in el:
                        wgs = transform(ordi)
                        c.append(str(wgs[1]) + ' ' + str(wgs[0]))
                    els.append('(' + ', '.join(c) + ')')
                cons.append('(' + ', '.join(els) + ')')
            geom = 'MULTIPOLYGON(' + ', '.join(cons) + ')'
        else: geom = None
        #print(geom)
        
        cur.execute("INSERT INTO farm_lands.lands_import\
                    (type, cadastral_number, subtype, common_land_cad_num, cat, permitted_use, area, region, district, full_address, cost, geom)\
                    VALUES ('{type}', '{cn}', '{subtype}', '{common_land_cad_num}', '{cat}', '{use}', {area}, '{region}', '{district}', '{full_address}', {cost}, {geom})\
                    ".format(type=d['type'] if d['type'] else 'NULL', 
                            cn=d['cadastral_number'] if d['cadastral_number'] else 'NULL', 
                            subtype=d['subtype'] if d['subtype'] else 'NULL', 
                            common_land_cad_num=d['common_land_cad_num'] if d['common_land_cad_num'] else 'NULL', 
                            cat=d['category'] if d['category'] else 'NULL', 
                            use = d['permitted_use'] if d['permitted_use'] else 'NULL',
                            area=d['area'] if d['area'] else 'NULL', 
                            region=d['region'] if d['region'] else 'NULL', 
                            district=d['district'] if d['district'] else 'NULL', 
                            full_address=d['full_address'] if d['full_address'] else 'NULL', 
                            cost=d['cost'] if d['cost'] else 'NULL', 
                            geom='\'' + geom + '\'' if geom else 'NULL'))
    conn.commit()