#coding utf-8
import os
import cherrypy
from app import view

class Index(object):

    def __init__(self, current_dir):
        self.view = view.View(current_dir)
        pass

    @cherrypy.expose
    def index(self):
	    return self.view.create("index.mako")

    @cherrypy.expose()
    def default(self, *arglist, **kwargs):
        msg_s = "no match: " + str(arglist) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)