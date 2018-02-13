# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.serloviews -t test_serloobjekt.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.serloviews.testing.EDI_SERLOVIEWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_serloobjekt.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Serloobjekt
  Given a logged-in site administrator
    and an add serloobjekt form
   When I type 'My Serloobjekt' into the title field
    and I submit the form
   Then a serloobjekt with the title 'My Serloobjekt' has been created

Scenario: As a site administrator I can view a Serloobjekt
  Given a logged-in site administrator
    and a serloobjekt 'My Serloobjekt'
   When I go to the serloobjekt view
   Then I can see the serloobjekt title 'My Serloobjekt'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add serloobjekt form
  Go To  ${PLONE_URL}/++add++Serloobjekt

a serloobjekt 'My Serloobjekt'
  Create content  type=Serloobjekt  id=my-serloobjekt  title=My Serloobjekt


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the serloobjekt view
  Go To  ${PLONE_URL}/my-serloobjekt
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a serloobjekt with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the serloobjekt title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
