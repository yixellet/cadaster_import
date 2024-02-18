from qgis.PyQt.QtCore import QVariant

fields = {
    'date_formation': {
        'type': QVariant.Date,
        'name': 'date_formation',
        'desc': 'Дата формирования выписки'
    },
    'organ_registr_rights': {
        'type': QVariant.String,
        'name': 'organ_registr_rights',
        'desc': 'Полное наименование органа регистрации прав'
    },
    'registration_number': {
        'type': QVariant.String,
        'name': 'registration_number',
        'desc': 'Регистрационный номер'
    },
    'full_name_position': {
        'type': QVariant.String,
        'name': 'full_name_position',
        'desc': 'Полное наименование должности'
    },
    'initials_surname': {
        'type': QVariant.String,
        'name': 'initials_surname',
        'desc': 'Инициалы, фамилия'
    },
    'cad_works': {
        'type': QVariant.String,
        'name': 'cad_works',
        'desc': 'Сведения о кадастровом инженере'
    },
    'address_type': {
        'type': QVariant.String,
        'name': 'address_type',
        'desc': 'Тип адреса'
    },
    'address': {
        'type': QVariant.String,
        'name': 'address',
        'desc': 'Адрес (местоположение)'
    },
    'rel_position': {
        'type': QVariant.String,
        'name': 'rel_position',
        'desc': 'Местоположение относительно ориентира'
    },
    'registration_date': {
        'type': QVariant.Date,
        'name': 'registration_date',
        'desc': 'Дата постановки на учет/регистрации'
    },
    'cancel_date': {
        'type': QVariant.Date,
        'name': 'cancel_date',
        'desc': 'Дата снятия с учета/регистрации'
    },
    'cad_number': {
        'type': QVariant.String,
        'name': 'cad_number',
        'desc': 'Кадастровый номер'
    },
    'type': {
        'type': QVariant.String,
        'name': 'type',
        'desc': 'Вид объекта недвижимости'
    },
    'area': {
        'type': QVariant.Int,
        'name': 'area',
        'desc': 'Площадь'
    },
    'volume': {
        'type': QVariant.Int,
        'name': 'volume',
        'desc': 'Объем'
    },
    'built_up_area': {
        'type': QVariant.Double,
        'name': 'built_up_area',
        'desc': 'Площадь застройки'
    },
    'height': {
        'type': QVariant.Double,
        'name': 'height',
        'desc': 'Высота'
    },
    'depth': {
        'type': QVariant.Double,
        'name': 'depth',
        'desc': 'Глубина'
    },
    'occurence_depth': {
        'type': QVariant.Double,
        'name': 'occurence_depth',
        'desc': 'Глубина залегания'
    },
    'area_inaccuracy': {
        'type': QVariant.Double,
        'name': 'area_inaccuracy',
        'desc': 'Погрешность площади'
    },
    'extension': {
        'type': QVariant.Double,
        'name': 'extension',
        'desc': 'Протяженность'
    },
    'area_type': {
        'type': QVariant.String,
        'name': 'area_type',
        'desc': 'Тип площади'
    },
    'land_use_by_document': {
        'type': QVariant.String,
        'name': 'land_use_by_document',
        'desc': 'По документу'
    },
    'land_use': {
        'type': QVariant.String,
        'name': 'land_use',
        'desc': 'Вид разрешенного использования земельного участка в соответствии с ранее использовавшимся классификатором'
    },
    'land_use_mer': {
        'type': QVariant.String,
        'name': 'land_use_mer',
        'desc': 'Вид разрешенного использования земельного участка в соответствии с классификатором'
    },
    'gr_reg_numb_border': {
        'type': QVariant.String,
        'name': 'gr_reg_numb_border',
        'desc': 'Реестровый номер границы'
    },
    'gr_land_use': {
        'type': QVariant.String,
        'name': 'gr_land_use',
        'desc': 'Вид разрешенного использования земельного участка в соответствии с классификатором'
    },
    'gr_permitted_use_text': {
        'type': QVariant.String,
        'name': 'gr_permitted_use_text',
        'desc': 'Разрешенное использование (текстовое описание)'
    },
    'ascendant_cad_numbers': {
        'type': QVariant.String,
        'name': 'ascendant_cad_numbers',
        'desc': 'Кадастровые номера земельных участков, из которых образован данный'
    },
    'descendant_cad_numbers': {
        'type': QVariant.String,
        'name': 'descendant_cad_numbers',
        'desc': 'Кадастровые номера земельных участков, образованных из данного'
    },
    'included_objects': {
        'type': QVariant.String,
        'name': 'included_objects',
        'desc': 'Кадастровые номера расположенных в пределах земельного участка объектов'
    },
    'facility_cad_number': {
        'type': QVariant.String,
        'name': 'facility_cad_number',
        'desc': 'Кадастровый номер предприятия как имущественного комплекса'
    },
    'old_numbers': {
        'type': QVariant.String,
        'name': 'old_numbers',
        'desc': 'Ранее присвоенные номера'
    },
    'common_land': {
        'type': QVariant.String,
        'name': 'common_land',
        'desc': 'Единое землепользование'
    },
    'land_cad_numbers': {
        'type': QVariant.String,
        'name': 'land_cad_numbers',
        'desc': 'Кадастровые номера иных объектов недвижимости (земельных участков)'
    },
    'common_land': {
        'type': QVariant.String,
        'name': 'common_land',
        'desc': 'Единое землепользование'
    },
    'floors': {
        'type': QVariant.String,
        'name': 'floors',
        'desc': 'Количество этажей'
    },
    'underground_floors': {
        'type': QVariant.String,
        'name': 'underground_floors',
        'desc': 'Количество подземных этажей'
    },
    'purpose': {
        'type': QVariant.String,
        'name': 'purpose',
        'desc': 'Назначение сооружения'
    },
    'name': {
        'type': QVariant.String,
        'name': 'name',
        'desc': 'Наименование сооружения'
    },
    'year_built': {
        'type': QVariant.String,
        'name': 'year_built',
        'desc': 'Год завершения строительства'
    },
    'year_commisioning': {
        'type': QVariant.String,
        'name': 'year_commisioning',
        'desc': 'Год ввода в эксплуатацию'
    },
}