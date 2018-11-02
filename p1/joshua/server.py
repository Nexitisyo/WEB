# coding: utf-8

import os
import sys
import cherrypy
from app import index
from app import mitarbeiter
from app import kunden
from app import projekte
#from var_dump import var_dump

def main():

    # --------------------------------------
    # Get current directory
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except:
        current_dir = os.path.dirname(os.path.abspath(sys.executable))
    # disable autoreload
    cherrypy.engine.autoreload.unsubscribe()
    # Static content config
    static_config = {
        '/': {
            'tools.staticdir.root': current_dir,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './content'
        }
    }
    config = {
        '/': {
            'tools.staticdir.root': current_dir,
            'tools.staticdir.on': False
        }
    }
    # Database.Database()
    # Mount static content handler
    cherrypy.tree.mount(index.Index(current_dir), '/', static_config)
    cherrypy.tree.mount(mitarbeiter.Mitarbeiter(current_dir), '/mitarbeiter/', config)
    cherrypy.tree.mount(kunden.Kunden(current_dir), '/kunden/', config)
    cherrypy.tree.mount(projekte.Projekte(current_dir), '/projekte/', config)
    # suppress traceback-info
    cherrypy.config.update({'request.show_tracebacks': False})
    cherrypy.config.update({'server.socket_port': 8080})
    # Start server
    cherrypy.engine.start()
    cherrypy.engine.block()


# --------------------------------------
if __name__ == '__main__':
    # --------------------------------------
    main()
# EOF
