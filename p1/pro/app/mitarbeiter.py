    #coding utf-8
import os
import cherrypy
from app import view

class Mitarbeiter(object):

    def __init__(self, current_dir):
        self.view = view.View(current_dir)
        pass

    @cherrypy.expose
    def index(self):
        return self.view.create("mitarbeiterDaten.mako")

    @cherrypy.expose()
    def create(self):
        return self.view.create("mitarbeiterForm.mako")

    @cherrypy.expose()
    def addEntry(self,funktion, name, vorname, key=None):

        return 












    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)