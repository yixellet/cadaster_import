import re

def cadLink(element, type):
    '''
    Кадастровые номера связанных объектов
    '''

    if element.find(type) != None:
        io = element.find(type)
        array = []
        for e in io.findall(type[:-1]):
            cn = e.find('cad_number').text
            cns = re.split('[,;]\s*', cn)
            array = array + cns
    else:
        array = None

    return array
