from .contours import quarter_contours

def quarter(root):
    """
    Извлекает инфо о кадастровом квартале из КПТ
    """
    result = {}
    cadastral_blocks = root.find('cadastral_blocks')
    cadastral_block = cadastral_blocks.find('cadastral_block')

    result['cadastral_number'] = cadastral_block.find('cadastral_number').text
    result['area'] = float(cadastral_block.find('area_quarter').find('area').text)
    result.update(quarter_contours(cadastral_block.find('spatial_data').find('entity_spatial')))
    result['content'] = 'quarters'
    result['geometryType'] = 'MultiPolygon'

    return result
