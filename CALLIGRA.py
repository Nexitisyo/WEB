import os, os.path
import random
import string

import cherrypy

cherrypy.config.update({'server.socket_port': 8080})


class site(object):
   	@cherrypy.expose
	def index(self):
	return "Hello world!"

if __name__ == '__main__':
    
    cherrypy.quickstart(site())