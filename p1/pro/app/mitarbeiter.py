#coding utf-8
import os
import cherrypy
from app import view

class Mitarbeiter(object):

    def __init__(self, current_dir):
        self.view = view.View(current_dir)
        pass

    @cherrypy.expose
    def index(self):
        return self.view.create("mitarbeiterDaten.mako")