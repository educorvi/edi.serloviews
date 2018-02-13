# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from edi.serloviews.testing import EDI_SERLOVIEWS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that edi.serloviews is properly installed."""

    layer = EDI_SERLOVIEWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edi.serloviews is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edi.serloviews'))

    def test_browserlayer(self):
        """Test that IEdiSerloviewsLayer is registered."""
        from edi.serloviews.interfaces import (
            IEdiSerloviewsLayer)
        from plone.browserlayer import utils
        self.assertIn(IEdiSerloviewsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDI_SERLOVIEWS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['edi.serloviews'])

    def test_product_uninstalled(self):
        """Test if edi.serloviews is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edi.serloviews'))

    def test_browserlayer_removed(self):
        """Test that IEdiSerloviewsLayer is removed."""
        from edi.serloviews.interfaces import \
            IEdiSerloviewsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEdiSerloviewsLayer, utils.registered_layers())
