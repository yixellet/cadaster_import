def parseEapl(root):
    '''
    Извлекает геометрию
    '''
    result = {}
    lr = root.find('land_record')

    # Описание местоположения границ ЗУ
    if lr.find('contours_location') != None:
        contAr = []
        for p in lr.find('contours_location').find('contours').findall('contour'):
            esArr = []
            es = p.find('entity_spatial')
            for e in es.find('spatials_elements').findall('spatial_element'):
                elAr = []
                for o in e.find('ordinates').findall('ordinate'):
                    elAr.append(' '.join([o.find('y').text, o.find('x').text]))
                elementWKT = '(' + ','.join(elAr) + ')'
                esArr.append(elementWKT)
            contourWKT = '(' + ','.join(esArr) + ')'
            contAr.append(contourWKT)
        geomWKT = 'MULTIPOLYGON(' + ','.join(contAr) + ')'
        result['geom'] = geomWKT
    
    return result