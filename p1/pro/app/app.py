import os
from mako.template import Template

import cherrypy

"""
• Verwaltung der Kundendaten
	◦ Anlegen, Ändern und Löschen von Kundendaten
	◦ Kundendaten sind z.B.
		▪ eindeutige Id
		▪ Nummer
		▪ Bezeichnung
		▪ Ansprechpartner
		▪ Ort
"""

class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		mytemplate = Template("hello world!")
		return print(mytemplate.render())

cherrypy.quickstart(HelloWorld())