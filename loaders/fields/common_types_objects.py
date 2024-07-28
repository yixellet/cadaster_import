"""Поля для атрибутивной информации, их типы и комментарии"""

from qgis.PyQt.QtCore import QMetaType

fields = {
    'material': {
        'type': QMetaType.QString,
        'name': 'material',
        'desc': 'Материал наружных стен здания'
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
    'full_name_position': {
        'type': QMetaType.QString,
        'name': 'full_name_position',
        'desc': 'Полное наименование должности'
    },
    'initials_surname': {
        'type': QMetaType.QString,
        'name': 'initials_surname',
        'desc': 'Инициалы, фамилия'
    },
    'date_received_request': {
        'type': QMetaType.QDateTime,
        'name': 'date_received_request',
        'desc': 'Дата поступившего запроса'
    },
    'date_receipt_request_reg_authority_rights': {
        'type': QMetaType.QDateTime,
        'name': 'date_receipt_request_reg_authority_rights',
        'desc': 'Дата получения запроса органом регистрации прав'
    }
}