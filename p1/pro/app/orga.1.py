# coding: utf-8

import cherrypy
from app import view
from app import database
import math

class Orga(object):

    def __init__(self, current_dir):

        self.view = view.View(current_dir)
        pass

    @cherrypy.expose()
    def index(self):

        return self.view.create("orga-form.mako", {
            "liste": database.read("projekte.json"),
    	    "liste2": database.read("mitarbeiter.json"),
            "liste3": database.read("orga.json")
        })

    @cherrypy.expose()
    def save(self, aufwandGeteilt, key=None):        
        if key:
            database.writeValuebyId("orga.json", key, {
                "aufwandGeteilt":aufwandGeteilt
            })

            raise cherrypy.HTTPRedirect("../orga/")
        else:

            database.append("orga.json", {
                "aufwandGeteilt":aufwandGeteilt
            })
            return self.index()

    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
