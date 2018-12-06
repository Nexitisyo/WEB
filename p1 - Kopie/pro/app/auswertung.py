# coding: utf-8

import cherrypy
from app import view
from app import database

class Auswertung(object):

    def __init__(self, current_dir):

        self.view = view.View(current_dir)
        pass

    @cherrypy.expose()
    def index(self):
        return self.view.create("auswertung.mako", {
            "liste": database.read("projekte.json"),
            "liste2": database.read("mitarbeiter.json")
        })

    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
