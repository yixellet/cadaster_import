# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'thaid@yandex.ru'
__date__ = '2024-02-03'
__copyright__ = 'Copyright 2024, Kirill Kotelevsky'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from cadaster_import_dockwidget import CadasterImportDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class CadasterImportDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = CadasterImportDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(CadasterImportDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

