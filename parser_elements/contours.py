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

def defineGeometryTypeET(spatialElement):
    '''
    Определеяет тип геометрии (полигон или линия)
    '''
    ordinates = spatialElement.find('ordinates')
    ordinatesArray = []
    for o in ordinates.findall('ordinate'):
        ordinatesArray.append((float(o.find('x').text), float(o.find('y').text)))
    firstPoint = ordinatesArray[0]
    lastPoint = ordinatesArray[-1]
    if firstPoint[0] == lastPoint[0] and firstPoint[1] == lastPoint[1]:
        return 'MultiPolygon'
    else:
        return 'MultiLineString'

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

def getGeometryInfo(element):
    '''
    Анализирует геометрию. Определяет:
        1. тип (линия или полигон)
        2. СК, указанную в XML
        3. извлекает образец координат
    '''
    result = {}
    p = element.find('contour')
    if p.find('cad_number') != None:
        result['cad_num'] = p.find('cad_number').text
    entitySpatial = p.find('entity_spatial')
    e = entitySpatial.find('spatials_elements').find('spatial_element')
    result['type'] = defineGeometryTypeET(e)
    ord = e.find('ordinates').find('ordinate')
    result['coord'] = [float(ord.find('x').text), float(ord.find('y').text)]
    y_ord = ord.find('y')
    result['msk_zone'] = int(y_ord[0])

    return result

def getMskZone(element) -> str:
    '''
    Анализирует геометрию. Определяет СК, указанную в XML.
    Функция принимает только элемент entity_spatial
    '''
    e = element.find('spatials_elements').find('spatial_element')
    ord = e.find('ordinates').find('ordinate')
    y_ord = ord.find('y')

    return y_ord[0]

def contours(element, transformate=False):
    '''
    Извлекает геометрию
    '''
    contoursArray = []
    geomType = 1
    zone = '1'
    for p in element.findall('contour'):
        spatialElementsArray = []
        if p.find('entity_spatial').find('spatials_elements') != None:
            es = p.find('entity_spatial')
            for e in es.find('spatials_elements').findall('spatial_element'):
                ordinatesArray = []
                ordinatesArrayMSK = []
                for o in e.find('ordinates').findall('ordinate'):
                    if transformate:
                        transformedOrdinate = transform([o.find('x').text, o.find('y').text], int(o.find('y').text[0]))
                    else:
                        transformedOrdinate = (o.find('x').text, o.find('y').text)
                    zone = o.find('y').text[0]
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
        else:
            return {'geom': None, 'msk_zone': None}

    if geomType == 1:
        geomWKT = 'MULTIPOLYGON(' + ','.join(contoursArray) + ')'
    else:
        geomWKT = 'MULTILINESTRING(' + ','.join(contoursArray) + ')'
        
    return {'geom': geomWKT, 'msk_zone': zone}

def quarter_contours(element):
    '''
    Извлекает геометрию из элемента entity_spatial
    Принимает на вход элемент entity_spatial
    '''
    contoursArray = []
    spatialElementsArray = []
    zone = '1'
    for e in element.find('spatials_elements').findall('spatial_element'):
        ordinatesArray = []
        for o in e.find('ordinates').findall('ordinate'):
            transformedOrdinate = (o.find('x').text, o.find('y').text)
            zone = o.find('y').text[0]
            ordinatesArray.append(' '.join([str(transformedOrdinate[1]), str(transformedOrdinate[0])]))
        elementWKT = '(' + ','.join(ordinatesArray) + ')'
        spatialElementsArray.append(elementWKT)
    contourWKT = '(' + ','.join(spatialElementsArray) + ')'
    contoursArray.append(contourWKT)
    geomWKT = 'MULTIPOLYGON(' + ','.join(contoursArray) + ')'
        
    return {'geom': geomWKT, 'msk_zone': zone}