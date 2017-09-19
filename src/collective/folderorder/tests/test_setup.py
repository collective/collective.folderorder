# -*- coding: utf-8 -*-
from collective.folderorder.testing import INTEGRATION_TESTING

import unittest


PROJECTNAME = 'collective.folderorder'


class InstallTestCase(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_user_action(self):
        object_buttons = self.portal['portal_actions'].object_buttons
        self.assertIn('order', object_buttons)

        permissions = object_buttons['order'].permissions
        expected = ('Manage properties',)
        self.assertEqual(permissions, expected)
        url_expr = object_buttons['order'].url_expr
        self.assertIn('string:$object_url/select_folder_order', url_expr)


class UninstallTestCase(unittest.TestCase):
    """Ensure product is properly uninstalled."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_user_action_removed(self):
        object_buttons = self.portal['portal_actions'].object_buttons
        self.assertNotIn('order', object_buttons)
