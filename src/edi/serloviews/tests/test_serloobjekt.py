# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from edi.serloviews.interfaces import ISerloobjekt
from edi.serloviews.testing import EDI_SERLOVIEWS_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class SerloobjektIntegrationTest(unittest.TestCase):

    layer = EDI_SERLOVIEWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Serloobjekt')
        schema = fti.lookupSchema()
        self.assertEqual(ISerloobjekt, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Serloobjekt')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Serloobjekt')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ISerloobjekt.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Serloobjekt',
            id='Serloobjekt',
        )
        self.assertTrue(ISerloobjekt.providedBy(obj))
