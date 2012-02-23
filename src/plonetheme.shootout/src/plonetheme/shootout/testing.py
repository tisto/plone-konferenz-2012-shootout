from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PlonethemeShootout(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import plonetheme.shootout
        xmlconfig.file('configure.zcml',
                       plonetheme.shootout,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.shootout:default')

PLONETHEME_SHOOTOUT_FIXTURE = PlonethemeShootout()
PLONETHEME_SHOOTOUT_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PLONETHEME_SHOOTOUT_FIXTURE, ),
                       name="PlonethemeShootout:Integration")