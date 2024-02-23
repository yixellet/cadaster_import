from pyproj import CRS, Transformer
from ..cadaster_import_utils import logMessage

def defineGeometryType(spatialElement):
    '''
    Определеяет тип геометрии (полигон или линия)
    '''
    firstPoint = spatialElement[0]
    lastPoint = spatialElement[-1]
    if firstPoint[0] == lastPoint[0] and firstPoint[1] == lastPoint[1]:
        return 1
    else:
        return 0

def transform(coords, zone=1):
    msk_1 = CRS.from_proj4('+proj=tmerc +lat_0=0 +lon_0=46.05 +k=1 +x_0=1300000 +y_0=-4714743.504 +ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs')
    msk_2 = CRS.from_proj4('+proj=tmerc +lat_0=0 +lon_0=49.05 +k=1 +x_0=2300000 +y_0=-4714743.504 +ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs')
    tr1 = Transformer.from_crs(msk_1, 4326)
    tr2 = Transformer.from_crs(msk_2, 4326)
    if zone == 1:
        wgs = tr1.transform(coords[1], coords[0])
    elif zone == 2:
        wgs = tr2.transform(coords[1], coords[0])
    else:
        logMessage('Неизвестная проекция: ' + coords[1] + coords[0])
        wgs = 'ERROR'
    return wgs

def analizeGeometry(element):
    '''
    Анализирует геометрию. Определяет:
        1. тип (линия или полигон)
        2. СК, указанную в XML
        3. извлекает образцы координат разных видов
    '''
    result = {}

def contours(element, transformate=True):
    '''
    Извлекает геометрию
    '''
    contoursArray = []
    geomType = 1
    for p in element.findall('contour'):
        spatialElementsArray = []
        es = p.find('entity_spatial')
        for e in es.find('spatials_elements').findall('spatial_element'):
            ordinatesArray = []
            ordinatesArrayMSK = []
            for o in e.find('ordinates').findall('ordinate'):
                if transformate:
                    transformedOrdinate = transform([o.find('x').text, o.find('y').text], int(o.find('y').text[0]))
                else:
                    transformedOrdinate = (o.find('x').text, o.find('y').text)
                ordinatesArray.append(' '.join([str(transformedOrdinate[1]), str(transformedOrdinate[0])]))
                ordinatesArrayMSK.append([float(o.find('x').text), float(o.find('y').text)])
            elementWKT = '(' + ','.join(ordinatesArray) + ')'
            spatialElementsArray.append(elementWKT)
            geomType = defineGeometryType(ordinatesArrayMSK)
        if geomType == 1:
            contourWKT = '(' + ','.join(spatialElementsArray) + ')'
            contoursArray.append(contourWKT)
        else:
            contourWKT = ','.join(spatialElementsArray)
            contoursArray.append(contourWKT)

    if geomType == 1:
        geomWKT = 'MULTIPOLYGON(' + ','.join(contoursArray) + ')'
    else:
        geomWKT = 'MULTILINESTRING(' + ','.join(contoursArray) + ')'
        
    return geomWKT