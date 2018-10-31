import os
from mako.template import Template
from mako.lookup import TemplateLookup

import cherrypy

#return in der Cherrypy Methode returned Werte oder einen Inhalt von etwas.
#In diesem Fall den Inhalt von Template welcher "I am alive" ist
#Dort kann auch eine Zieldatei angegeben werden mit
mytemplate = Template(filename='C:/WEB/p1/pro/template/liste.tpl')
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

class main(object):
	@cherrypy.expose
	def index(self):
		return mytemplate.render()


cherrypy.quickstart(main())