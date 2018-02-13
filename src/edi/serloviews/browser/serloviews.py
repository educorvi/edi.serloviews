import requests
from zope.interface import Interface
from uvc.api import api

api.templatedir('templates')

class Serloview(api.Page):
    api.context(Interface)

    def update(self):
        headers = {'Accept': 'application/json'}
        results = requests.get(self.context.remoteUrl, headers=headers,)        
        self.lernobjekte = results.json() 
