def detailsStatement(element):
    '''
    Извлекает сведения о выписке / КПТ
    '''
    result = {}
    ds = element.find('details_statement')

    # "Высшие реквизиты" - номер и дата выписки
    gtr = ds.find('group_top_requisites')
    if gtr.find('registration_number') != None:
        result['registration_number'] = gtr.find('registration_number').text
    else:
        result['registration_number'] = None
    result['date_formation'] = gtr.find('date_formation').text

    # "Низшие реквизиты" - должность и имя регистратора
    if ds.find('group_lower_requisites') != None:
        result['position'] = ds.find('group_lower_requisites').find('full_name_position').text
        result['name'] = ds.find('group_lower_requisites').find('initials_surname').text
    else:
        result['full_name_position'] = None
        result['initials_surname'] = None
    
    return result