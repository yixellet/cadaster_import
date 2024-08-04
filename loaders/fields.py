"""Поля для атрибутивной информации, их типы и комментарии"""

from qgis.PyQt.QtCore import QMetaType

fields = {
    'date_formation': {
        'type': QMetaType.QDateTime,
        'name': 'date_formation',
        'desc': 'Дата формирования выписки'
    },
    'organ_registr_rights': {
        'type': QMetaType.QString,
        'name': 'organ_registr_rights',
        'desc': 'Полное наименование органа регистрации прав'
    },
    'registration_number': {
        'type': QMetaType.QString,
        'name': 'registration_number',
        'desc': 'Регистрационный номер'
    },
    'registration_date': {
        'type': QMetaType.QDateTime,
        'name': 'registration_date',
        'desc': 'Дата регистрации'
    },
    'full_name_position': {
        'type': QMetaType.QString,
        'name': 'full_name_position',
        'desc': 'Полное наименование должности'
    },
    'name_by_doc': {
        'type': QMetaType.QString,
        'name': 'name_by_doc',
        'desc': 'Вид или наименование по документу'
    },
    'initials_surname': {
        'type': QMetaType.QString,
        'name': 'initials_surname',
        'desc': 'Инициалы, фамилия'
    },
    'cad_works': {
        'type': QMetaType.QString,
        'name': 'cad_works',
        'desc': 'Сведения о кадастровом инженере'
    },
    'subtype': {
        'type': QMetaType.QString,
        'name': 'subtype',
        'desc': 'Подтип'
    },
    'address_type': {
        'type': QMetaType.QString,
        'name': 'address_type',
        'desc': 'Тип адреса'
    },
    'address': {
        'type': QMetaType.QString,
        'name': 'address',
        'desc': 'Адрес (местоположение)'
    },
    'rel_position': {
        'type': QMetaType.QString,
        'name': 'rel_position',
        'desc': 'Местоположение относительно ориентира'
    },
    'cancel_date': {
        'type': QMetaType.QDateTime,
        'name': 'cancel_date',
        'desc': 'Дата снятия с учета/регистрации'
    },
    'cad_number': {
        'type': QMetaType.QString,
        'name': 'cad_number',
        'desc': 'Кадастровый номер'
    },
    'cadastral_number': {
        'type': QMetaType.QString,
        'name': 'cadastral_number',
        'desc': 'Кадастровый номер квартала'
    },
    'quartal': {
        'type': QMetaType.QString,
        'name': 'quartal',
        'desc': 'Кадастровый номер квартала'
    },
    'type': {
        'type': QMetaType.QString,
        'name': 'type',
        'desc': 'Вид объекта недвижимости'
    },
    'type_boundary': {
        'type': QMetaType.QString,
        'name': 'type_boundary',
        'desc': 'Вид границы'
    },
    'type_zone': {
        'type': QMetaType.QString,
        'name': 'type_zone',
        'desc': 'Вид зоны'
    },
    'water': {
        'type': QMetaType.QString,
        'name': 'water',
        'desc': 'Водный объект'
    },
    'area': {
        'type': QMetaType.Double,
        'name': 'area',
        'desc': 'Площадь'
    },
    'volume': {
        'type': QMetaType.Int,
        'name': 'volume',
        'desc': 'Объем'
    },
    'built_up_area': {
        'type': QMetaType.Double,
        'name': 'built_up_area',
        'desc': 'Площадь застройки'
    },
    'height': {
        'type': QMetaType.Double,
        'name': 'height',
        'desc': 'Высота'
    },
    'depth': {
        'type': QMetaType.Double,
        'name': 'depth',
        'desc': 'Глубина'
    },
    'occurence_depth': {
        'type': QMetaType.Double,
        'name': 'occurence_depth',
        'desc': 'Глубина залегания'
    },
    'area_inaccuracy': {
        'type': QMetaType.Double,
        'name': 'area_inaccuracy',
        'desc': 'Погрешность площади'
    },
    'extension': {
        'type': QMetaType.Double,
        'name': 'extension',
        'desc': 'Протяженность'
    },
    'area_type': {
        'type': QMetaType.QString,
        'name': 'area_type',
        'desc': 'Тип площади'
    },
    'land_use_by_document': {
        'type': QMetaType.QString,
        'name': 'land_use_by_document',
        'desc': 'По документу'
    },
    'land_use': {
        'type': QMetaType.QString,
        'name': 'land_use',
        'desc': 'Вид разрешенного использования земельного участка в соответствии с ранее использовавшимся классификатором'
    },
    'land_use_mer': {
        'type': QMetaType.QString,
        'name': 'land_use_mer',
        'desc': 'Вид разрешенного использования земельного участка в соответствии с классификатором'
    },
    'gr_reg_numb_border': {
        'type': QMetaType.QString,
        'name': 'gr_reg_numb_border',
        'desc': 'Реестровый номер границы'
    },
    'reg_numb_border': {
        'type': QMetaType.QString,
        'name': 'reg_numb_border',
        'desc': 'Реестровый номер границы'
    },
    'gr_land_use': {
        'type': QMetaType.QString,
        'name': 'gr_land_use',
        'desc': 'Вид разрешенного использования земельного участка в соответствии с классификатором'
    },
    'gr_permitted_use_text': {
        'type': QMetaType.QString,
        'name': 'gr_permitted_use_text',
        'desc': 'Разрешенное использование (текстовое описание)'
    },
    'ascendant_cad_numbers': {
        'type': QMetaType.QString,
        'name': 'ascendant_cad_numbers',
        'desc': 'Кадастровые номера земельных участков, из которых образован данный'
    },
    'descendant_cad_numbers': {
        'type': QMetaType.QString,
        'name': 'descendant_cad_numbers',
        'desc': 'Кадастровые номера земельных участков, образованных из данного'
    },
    'included_objects': {
        'type': QMetaType.QString,
        'name': 'included_objects',
        'desc': 'Кадастровые номера расположенных в пределах земельного участка объектов'
    },
    'facility_cad_number': {
        'type': QMetaType.QString,
        'name': 'facility_cad_number',
        'desc': 'Кадастровый номер предприятия как имущественного комплекса'
    },
    'old_numbers': {
        'type': QMetaType.QString,
        'name': 'old_numbers',
        'desc': 'Ранее присвоенные номера'
    },
    'common_land_cad_number': {
        'type': QMetaType.QString,
        'name': 'common_land_cad_number',
        'desc': 'Кадастровый номер единого землепользования'
    },
    'number': {
        'type': QMetaType.QString,
        'name': 'number',
        'desc': 'Номер'
    },
    'land_cad_numbers': {
        'type': QMetaType.QString,
        'name': 'land_cad_numbers',
        'desc': 'Кадастровые номера иных объектов недвижимости (земельных участков)'
    },
    'floors': {
        'type': QMetaType.QString,
        'name': 'floors',
        'desc': 'Количество этажей'
    },
    'underground_floors': {
        'type': QMetaType.QString,
        'name': 'underground_floors',
        'desc': 'Количество подземных этажей'
    },
    'purpose': {
        'type': QMetaType.QString,
        'name': 'purpose',
        'desc': 'Назначение сооружения'
    },
    'name': {
        'type': QMetaType.QString,
        'name': 'name',
        'desc': 'Наименование сооружения'
    },
    'year_built': {
        'type': QMetaType.QString,
        'name': 'year_built',
        'desc': 'Год завершения строительства'
    },
    'year_commisioning': {
        'type': QMetaType.QString,
        'name': 'year_commisioning',
        'desc': 'Год ввода в эксплуатацию'
    },
}