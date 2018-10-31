import os
from mako.template import Template
from mako.lookup import TemplateLookup

import cherrypy

#return in der Cherrypy Methode returned Werte oder einen Inhalt von etwas.
#In diesem Fall den Inhalt von Template welcher "I am alive" ist
#Dort kann auch eine Zieldatei angegeben werden mit
index = Template(filename='C:/WEB/p1/pro/template/startseite.tpl')
create = Template(filename='C:/WEB/p1/pro/template/create.tpl')
edit = Template(filename='C:/WEB/p1/pro/template/edit.tpl')
delete = Template(filename='C:/WEB/p1/pro/template/delete.tpl')

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
		return index.render()
	
	@cherrypy.expose
	def create(self):
		return ''.join(create.render())
	
	@cherrypy.expose
	def edit(self):
		return edit.render()

	@cherrypy.expose
	def delete(self):
		return delete.render()


cherrypy.quickstart(main()) 