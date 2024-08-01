from xml.etree.ElementTree import Element

class ParserElements():
    """
    Инструменты парсинга элементов, общих для всех типов XML
    """
    def __init__(self) -> None:
        pass


    def parse_dict(root: Element,
                   export_element: str = 'value') -> str:
        """
        Извлекает данные, представленные в форме словаря

        :param export_value: Что необходимо извлечь из словаря 
        (code или value), по умолчанию value
        :type export_value: str, optional
        :return: Возвращает строку - код или значение
        :rtype: str
        """
        return root.find(export_element).text


    def parse_common_data(self, root: Element) -> dict[str, str]:
        """Извлекает кадастровый номер и тип объекта"""
        result = {}
        cd = root.find('common_data')
        result['cad_number'] = cd.find('cad_number').text
        result['quarter_cad_number'] = cd.find('quarter_cad_number').text
        result['type'] = self.parse_dict(cd.find('type'))

        return result
    
    def parse_record_info(element: Element) -> dict[str, str]:
        """
        Извлекает даты государственной регистрации 
        (постановки/снятия с учета (регистрации))
        """
        result = {}
        result['registration_date'] = element.find('registration_date').text
        cancel_date = element.find('cancel_date')
        if cancel_date != None:
            result['cancel_date'] = cancel_date.text
        else:
            result['cancel_date'] = None

        return result
