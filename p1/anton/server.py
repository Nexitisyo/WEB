import os
import sys
import cherrypy
from app.application import Application


def main():
    try:
        project_dir = os.path.dirname(os.path.abspath(__file__))
    except:
        project_dir = os.path.dirname(os.path.abspath(sys.executable))
    cherrypy.engine.autoreload.unsubscribe()
    static_config = {
            '/': {
                'tools.staticdir.root': project_dir,
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './content'
            }
        }
    root = cherrypy.tree.mount(Application(project_dir), '/', static_config)

    cherrypy.config.update({'request.show_tracebacks': False})
# Start server
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()
