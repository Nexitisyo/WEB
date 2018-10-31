import cherrypy

from .database import CDatabase
from .view import CView

class CApplication(object):
    def __init__(self, project_dir):
        self.db = CDatabase(project_dir)
        self.view = CView(project_dir)

    def create_list(self):
        data = self.db.read()

        return self.view.create_list(data)

    def create_form(self, id = None):
        data = None
        if id != None:
            data = self.db.read(id)

        print("ID: ", id)
        print("DATA: ", data)

        return self.view.create_form(data)

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
        id = data_args["matriculation"]
        data = [data_args["forename"], data_args["surname"], data_args["session"], data_args["department"]]

        status = False

        if id != "None":
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

