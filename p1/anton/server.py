import os
import sys
import cherrypy
from app import application

def main():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except:
        current_dir = os.path.dirname(os.path.abspath(sys.executable))
        #disable autoreload
    #cherrypy.engine.autoreload.unsubscribe()
        #static content config
    static_config = {
            '/': {
                'tools.staticdir.root': current_dir,
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './content'
            }
        }
# Mount static content handler
    root_o = cherrypy.tree.mount(application.CApplication(current_dir), '/', static_config)
# suppress traceback-info
    cherrypy.config.update({'request.show_tracebacks': False})
# Start server
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()