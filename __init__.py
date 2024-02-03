# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CadasterImport
                                 A QGIS plugin
 Imports XML files from russian state land register
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-02-03
        copyright            : (C) 2024 by Kirill Kotelevsky
        email                : thaid@yandex.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CadasterImport class from file CadasterImport.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cadaster_import import CadasterImport
    return CadasterImport(iface)
