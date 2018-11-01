import cherrypy

from .database import CDatabase
from .view import CView

class CApplication(object):
    def __init__(self, project_dir):
        self.db = CDatabase(project_dir)
        self.view = CView(project_dir)
        self.data = self.db.read()
        print(self.data)

    def create_list(self):
        return self.view.create_list(self.data)

    def create_form(self, id = None):
        data = None
        if id != None:
            data = self.db.read(id)
            keys = self.get_keys()
            return self.view.create_form(id, data, keys)
        else:
            return self.view.create_form(None, {}, [])


    def get_keys(self):
        keys = list()
        for key in self.data:
            keys.append(key)
        return keys

#web application methods
    @cherrypy.expose
    def index(self):
        return self.create_list()

    @cherrypy.expose
    def add(self):
        return self.create_form()

    @cherrypy.expose
    def edit(self, id):
        return self.create_form(id)

    @cherrypy.expose
    def save(self, **data_args):
        #data_args: dictionary with key-value-pairs
        #TODO check if data is correct
        id = None
        if "matriculation" in data_args:
            id = data_args.pop("matriculation")
        data = data_args
        status = False

        keys = self.get_keys()
        if id in keys:
            status = self.db.update(id, data)
        else:
            status = True
            id = self.db.create(data)

        #TODO: Needs improved status checking
        if status == False:
            exit(1)
        return self.create_form(id)

    @cherrypy.expose
    def delete(self, id):
        self.db.delete(id)
        return self.create_list()

    @cherrypy.expose
    def default(self, *arguments, **kwargs):
        msg = "unbekannte Anforderung: " + str(arguments) + ' ' + str(kwargs)
        raise cherrypy.HTTPError(404, msg)
    default.exposed = True

