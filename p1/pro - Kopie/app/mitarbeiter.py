# coding: utf-8

import cherrypy
from app import view
from app import database


class Mitarbeiter(object):

    def __init__(self, current_dir):

        self.view = view.View(current_dir)
        pass

    @cherrypy.expose()
    def index(self):

        return self.view.create("mitarbeiter.mako", {
            "liste": database.read("mitarbeiter.json")
        })

    @cherrypy.expose()
    def save(self, funktion, name, vorname, key=None):
        if key:
            database.writeValuebyId("mitarbeiter.json", key, {
                "funktion": funktion,
                "name": name,
                "vorname": vorname
            })

            raise cherrypy.HTTPRedirect("../mitarbeiter/")
        else:

            database.append("mitarbeiter.json", {
                "funktion": funktion,
                "name": name,
                "vorname": vorname
            })
            return self.index()

    @cherrypy.expose()
    def add(self):
        return self.view.create("mitarbeiter-form.mako")

    @cherrypy.expose()
    def delete(self, key):
        database.deleteValueById("mitarbeiter.json", key)
        return self.index()

    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)

    @cherrypy.expose()
    def edit(self, key):
        try:
            mitarbeiter = database.readValuebyId("mitarbeiter.json", key)
        except Exception:
            return self.default()

        return self.view.create("mitarbeiter-form.mako", {
            "mitarbeiter": mitarbeiter,
            "action": "edit"
        })
