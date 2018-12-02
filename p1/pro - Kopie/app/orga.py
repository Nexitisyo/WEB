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
    def save(self, aufwandGeteilt, bezeichnung, mitarbeiter, key=None):     
        mliste = mitarbeiter
        tmpGeteilt = []

        if type(mitarbeiter) is not list:
            mliste = []
            mliste.append(mitarbeiter)
            
        if type(aufwandGeteilt) is not int:
            ###################################
            if type(aufwandGeteilt) is list: 
                for item,index in enumerate(aufwandGeteilt):
                    print(item,index)
                    tmp = aufwandGeteilt[item]
                    tmp = int(tmp)
                    tmpGeteilt.append(tmp)
            ###################################
            else: 
                tmp = int(aufwandGeteilt)
                aufwandGeteilt = []
                aufwandGeteilt.append(tmp)
            
        aufwandGeteilt = tmpGeteilt

        if key:
            database.writeValuebyId("orga.json", key, {
                
                "bezeichnung": bezeichnung,
                "mitarbeiter": mliste,
                "aufwandGeteilt":aufwandGeteilt
            })

            raise cherrypy.HTTPRedirect("../projekte/")
   
    @cherrypy.expose()
    def edit(self, key):
        try:
            projekt = database.readValuebyId("projekte.json", key)
            orga = database.readValuebyId("orga.json", key)
        except Exception:
            return self.default()

        return self.view.create("orga-form.mako", {
            "projekte": projekt,
            "orga": orga,
            "liste": database.read("kunden.json"),
            "liste2": database.read("mitarbeiter.json"),
            "liste3": database.read("orga.json"),
            "action": "edit"
        })

    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
