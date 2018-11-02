# coding: utf-8

import cherrypy
from app import view


class Index(object):

    def __init__(self, current_dir): # __init__.py sorgt dafür, dass Python '.py' - Dateien als Module erkennt.
        #def __init__ = Konstruktor
        #self = erlaubt Zugriff auf Attribute und Methoden der class

        self.view = view.View(current_dir)
        pass #Placeholder damit der Server nicht abschmiert

    @cherrypy.expose() #Macht Methoden für den Benutzer sichtbar/zugreifbar
    def index(self):
        return self.view.create("index.mako")

    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
