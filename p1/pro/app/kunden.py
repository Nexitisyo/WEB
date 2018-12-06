# coding: utf-8
import cherrypy
from app import view
from app import database

class Kunden(object):

    def __init__(self, current_dir):

        self.view = view.View(current_dir) #Fragen was das genau macht
        pass

    @cherrypy.expose()
    def index(self):

        return self.view.create("kunden.mako", {
            "liste": database.read("kunden.json")
        })

        #return self.view.create("kunden.mako", {"liste": database.read("kunden.json")})


    @cherrypy.expose()
    def save(self, kundennummer, bezeichnung, ansprechpartner, ort, key=None):
        if key: #Ist key hier durch key=None initialisiert? Fragen!
            database.writeValuebyId("kunden.json", key, {
                "kundennummer": kundennummer,
                "bezeichnung": bezeichnung,
                "ansprechpartner": ansprechpartner,
                "ort": ort
            })

            raise cherrypy.HTTPRedirect("../kunden/")
        else:

            database.append("kunden.json", {
                "kundennummer": kundennummer,
                "bezeichnung": bezeichnung,
                "ansprechpartner": ansprechpartner,
                "ort": ort
            })
            return self.index()

    @cherrypy.expose()
    def add(self):
        return self.view.create("kunden-form.mako")

    @cherrypy.expose()
    def delete(self, key):
        splitID = key.split(",")
        database.deleteValueById("kunden.json", splitID)
        return self.index()
        
    @cherrypy.expose()
    def edit(self, key):
        try:
            kunden = database.readValuebyId("kunden.json", key)
        except Exception:
            return self.default()

        return self.view.create("kunden-form.mako", {
            "kunden": kunden,
            "action": "edit"
        })

    @che    rrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)


