# coding: utf-8

import cherrypy
from app import view
from app import database
import math

class Projekte(object):

    def __init__(self, current_dir):

        self.view = view.View(current_dir)
        pass

    @cherrypy.expose()
    def index(self):

        return self.view.create("projekte.mako", {
            "liste": database.read("projekte.json"),
    	    "liste2": database.read("mitarbeiter.json"),
            "liste3": database.read("orga.json")
        })

    @cherrypy.expose()
    def save(self, projektnummer, bezeichnung, beschreibung, bearbeitungszeitraumA, bearbeitungszeitraumB, budget, kundenverweis,
             mitarbeiterverweis:list, key=None):
        
        mliste = mitarbeiterverweis
        if type(mitarbeiterverweis) is str:
            mliste = [mitarbeiterverweis]

        if (bearbeitungszeitraumA == None) or (bearbeitungszeitraumB == None):
            bearbeitungszeitraumA = "invalid date"
            bearbeitungszeitraumB = "invalid date"
        else:
            differenceInDays = database.calc(bearbeitungszeitraumA, bearbeitungszeitraumB)
            differenceWeeks = differenceInDays / 7
        
        if key:
            database.writeValuebyId("projekte.json", key, {
                "projektnummer": projektnummer,
                "bezeichnung": bezeichnung,
                "beschreibung": beschreibung,
                "bearbeitungszeitraumA": bearbeitungszeitraumA,
                "bearbeitungszeitraumB": bearbeitungszeitraumB,
                "budget": budget,
                "kundenverweis": kundenverweis,
                "mitarbeiterverweis": mliste,
                "aufwand": differenceInDays,
                "aufwandWeek": differenceWeeks
            })

            database.writeValuebyId("orga.json", key, {
                "projektnummer": projektnummer,
                "bezeichnung": bezeichnung,
                "mitarbeiter": mitarbeiterverweis,
                "aufwand": differenceInDays
            })

            raise cherrypy.HTTPRedirect("../projekte/")
        else:
            database.append("projekte.json", {
                "projektnummer": projektnummer,
                "bezeichnung": bezeichnung,
                "beschreibung": beschreibung,
                "bearbeitungszeitraumA": bearbeitungszeitraumA,
                "bearbeitungszeitraumB": bearbeitungszeitraumB,
                "budget": budget,
                "kundenverweis": kundenverweis,
                "mitarbeiterverweis": mliste,
                "aufwand": differenceInDays,
                "aufwandWeek": differenceWeeks
            })

            database.append("orga.json", {
                "projektnummer": projektnummer,
                "bezeichnung": bezeichnung,
                "mitarbeiter": mliste,
                "aufwand": differenceInDays
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
        database.deleteValueById("orga.json", key)
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
