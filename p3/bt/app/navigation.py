# coding: utf-8
import cherrypy
from .database import Database_cl


class Navigation_cl(object):
    exposed = True

    def __init__(self, path):
        self.db = Database_cl(path)

    @cherrypy.tools.json_out()
    def GET(self, roleId):
        commonNav = [{
            "target": "fehler",
            "action": "list-view",
            "name": "Übersicht Fehler"
        }, {
            "target": "projekt",
            "action": "list-view",
            "name": "Übersicht Projekte"
        }, {
            "target": "komponente",
            "action": "list-view",
            "name": "Übersicht Komponenten"
        }, {
            "target": "employee",
            "action": "list-view",
            "name": "Übersicht Mitarbeiter"
        }, {
            "target": "category",
            "action": "list-view",
            "name": "Übersicht Kategorien"
        }, {
            "target": "",
            "action": "eval-pro-err",
            "name": "Auswertung Projektfehler"
        }, {
            "target": "",
            "action": "eval-cat-err",
            "name": "Auswertung Kategoriefehler"
        },
        ]
        if int(roleId) == 1:
            # The user is a QS-Mitarbeiter
            qsNav = [{
                "target": "fehler",
                "action": "add-item",
                "name": "Neuer Fehler"
            }]
            return qsNav + commonNav
        elif int(roleId) == 2:
            # The user is a SE-Mitarbeiter
            seNav = []
            return seNav + commonNav
        raise cherrypy.HTTPError(404, "Interner Fehler aufgetreten!")
# EOF
