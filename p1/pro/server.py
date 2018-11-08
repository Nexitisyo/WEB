# coding: utf-8
import os
import sys
import cherrypy
from app import index
from app import mitarbeiter
from app import kunden
from app import projekte
from app import auswertung 
from app import orga#import projekte etc. aus dem Ordner app
#from var_dump import var_dump

def main():
    # --------------------------------------
    # Get current directory
    # -------------------------------------
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__)) #derzeitiges Verzeichnis von server.py
    except:
        current_dir = os.path.dirname(os.path.abspath(sys.executable))
    # disable autoreload
    cherrypy.engine.autoreload.unsubscribe()

    # Static content config
    static_config = {
        '/': {
            'tools.staticdir.root': current_dir, #serving whole directory current_directory (server.py)
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './content'  #mapping /content with localhost deswegen localhost/style.css aufrufbar
        }
    }
    config = {
        '/': {
            'tools.staticdir.root': current_dir,
            'tools.staticdir.on': False
        }
    }

    # Database.Database()
    # Mount static content handler = Mehrere Seiten laden (einzelne mit cherrypy.quickstart())
    cherrypy.tree.mount(index.Index(current_dir), '/', static_config)
    cherrypy.tree.mount(mitarbeiter.Mitarbeiter(current_dir), '/mitarbeiter/', config)
    cherrypy.tree.mount(kunden.Kunden(current_dir), '/kunden/', config)
    cherrypy.tree.mount(projekte.Projekte(current_dir), '/projekte/', config)
    cherrypy.tree.mount(auswertung.Auswertung(current_dir), '/auswertung/', config)
    cherrypy.tree.mount(orga.Orga(current_dir), '/orga/', config)

    # suppress traceback-info
    cherrypy.config.update({'request.show_tracebacks': True}) #Errors nicht anzeigen/anzeigen (404, 500, etc)
    cherrypy.config.update({'server.socket_port': 8080})

    # Start server
    cherrypy.engine.start()
    cherrypy.engine.block()


# --------------------------------------
if __name__ == '__main__':
    # --------------------------------------
    main()
# EOF
