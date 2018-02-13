# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.serloviews


class EdiSerloviewsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=edi.serloviews)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.serloviews:default')


EDI_SERLOVIEWS_FIXTURE = EdiSerloviewsLayer()


EDI_SERLOVIEWS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_SERLOVIEWS_FIXTURE,),
    name='EdiSerloviewsLayer:IntegrationTesting'
)


EDI_SERLOVIEWS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_SERLOVIEWS_FIXTURE,),
    name='EdiSerloviewsLayer:FunctionalTesting'
)


EDI_SERLOVIEWS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_SERLOVIEWS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EdiSerloviewsLayer:AcceptanceTesting'
)
