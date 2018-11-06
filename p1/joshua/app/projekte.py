# coding: utf-8

import cherrypy
from app import view
from app import database


class Projekte(object):

    def __init__(self, current_dir):

        self.view = view.View(current_dir)
        pass

    @cherrypy.expose()
    def index(self):

        return self.view.create("projekte.mako", {
            "liste": database.read("projekte.json"),
    	    "liste2": database.read("mitarbeiter.json")
        })

    @cherrypy.expose()
    def save(self, projektnummer, bezeichnung, beschreibung, bearbeitungszeitraum, budget, kundenverweis,
             mitarbeiterverweis, aufwand, key=None):

        if key:
            database.writeValuebyId("projekte.json", key, {
                "projektnummer": projektnummer,
                "bezeichnung": bezeichnung,
                "beschreibung": beschreibung,
                "bearbeitungszeitraum": bearbeitungszeitraum,
                "budget": budget,
                "kundenverweis": kundenverweis,
                "mitarbeiterverweis": mitarbeiterverweis,
                "aufwand": aufwand
            })

            raise cherrypy.HTTPRedirect("../projekte/")
        else:

            database.append("projekte.json", {
                "projektnummer": projektnummer,
                "bezeichnung": bezeichnung,
                "beschreibung": beschreibung,
                "bearbeitungszeitraum": bearbeitungszeitraum,
                "budget": budget,
                "kundenverweis": kundenverweis,
                "mitarbeiterverweis": mitarbeiterverweis,
                "aufwand": aufwand
            })
            return self.index()

    @cherrypy.expose()
    def add(self):
        return self.view.create("projekte-form.mako",{
            "liste": database.read("kunden.json"),
            "liste2": database.read("mitarbeiter.json")
        })

    @cherrypy.expose()
    def delete(self, key):
        database.deleteValueById("projekte.json", key)
        return self.index()

    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)

    @cherrypy.expose()
    def edit(self, key):
        try:
            projekt = database.readValuebyId("projekte.json", key)
        except Exception:
            return self.default()

        return self.view.create("projekte-form.mako", {
            "projekte": projekt,
            "liste": database.read("kunden.json"),
            "liste2": database.read("mitarbeiter.json"),
            "action": "edit"
        })
