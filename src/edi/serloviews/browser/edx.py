# -*- coding: utf-8 -*-
from zope.interface import Interface
from uvc.api import api
from plone import api as ploneapi
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

bodytext = u"""\
<h2>Das ist ein Beispieltext.</h2>

<p>Das ist ein Beispieltext. Bitte formatieren Sie diesen Text mit den Werkzeugen des Editors so, wie Sie das im OPENedX-Kurs gelernt haben.</p>

<p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund!« 
sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem 
Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele 
ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu 
dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch 
ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem 
Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, umdrängten den 
Käfig und wollten sich gar nicht fortrühren. Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er 
eines Morgens verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen 
Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen 
Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher 
Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten 
Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt 
sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, 
umdrängten den Käfig und wollten sich gar nicht fortrühren. Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, 
wurde er eines Morgens verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus 
unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer 
neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein 
eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch 
wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen 
damit und hielt sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber 
sie überwanden sich, umdrängten den Käfig und wollten sich gar nicht fortrühren.Jemand musste Josef K. verleumdet haben, denn ohne dass er 
etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben.</p>"""

linktext = u"""\
<h2>Das ist ein Beispieltext</h2>

<p>Das ist ein Beispieltext. Bitte verlinken Sie die Inhalte extern und intern so wie Sie es im Tutorial gelernt haben.</p>

<p>Ein interner Link auf einen Ordner oder ein Dokument im Portal</p>
<p>Ein externer Link auf eine Seite im Online-Magazin Spiegel</p>

"""

embedtext = u"""\
<h2>Das ist ein Beispieltext</h2>

<p>Das ist ein Beispieltext. Bitte betten Sie hier ein Video und ein Bild ein.</p>

<p>[Hier betten Sie ein Video ein.]</p>
<p>[Hier fügen Sie ein Bild ein.]</p>
"""

api.templatedir('templates')

class EditorView(api.Page):
    api.context(Interface)

    def update(self):
        alsoProvides(self.request, IDisableCSRFProtection)

    def render(self):
        mytext = bodytext
        if self.request.get('what') == 'link':
            mytext = linktext
        if self.request.get('what') == 'embed':
            mytext = embedtext
        if self.request.get('what') == 'body':
            mytext = bodytext
        alsoProvides(self.request, IDisableCSRFProtection)
        obj = ploneapi.content.create(
            type="Document",
            title="Test aus OPENedX",
            text=mytext,
            container=self.context)
        url = obj.absolute_url() + '/edit'
        return self.response.redirect(url)

class AudioView(api.View):
    api.context(Interface)
