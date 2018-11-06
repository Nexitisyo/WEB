    #coding utf-8
import os
import cherrypy
from app import view
from app import db

class Mitarbeiter(object):

    def __init__(self, current_dir):
        self.view = view.View(current_dir)
        pass

    @cherrypy.expose
    def index(self):
        return self.view.create("mitarbeiterDaten.mako",{
            "liste": db.read("mitarbeiter.json")
        })

    @cherrypy.expose()
    def create(self):
        return self.view.create("mitarbeiterForm.mako")

    @cherrypy.expose()
    def addEntry(self,funktion, name, vorname, key=None):
        if key:
            db.updateJson("mitarbeiter.json",{
                "funktion": funktion,
                "name": name,
                "vorname": vorname                
            })
            raise cherrypy.HTTPRedirect("../kunden/")
        else:
            db.append("mitarbeiter.json",{
                "funktion": funktion,
                "name": name,
                "vorname": vorname
            })
            return self.index()












    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)