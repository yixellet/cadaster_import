def recordInfo(element):
    '''
    Извлекает Даты государственной регистрации
    '''

    result = {}
    result['registration_date'] = element.find('registration_date').text
    if element.find('cancel_date') != None:
        result['cancel_date'] = element.find('cancel_date').text
    else:
        result['cancel_date'] = None

    return result
