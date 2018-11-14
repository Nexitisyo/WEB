import codecs
import os.path

import cherrypy

from .project import Project
from .employee import Employee
from .customer import Customer
from .registration import Registration
from .hours import Hours

from .database import Encoding, FileMode
from .view import View


class Application(object):
    def __init__(self, project_dir):
        self.project_dir = project_dir
        self.view = View(project_dir)
        self.index_path = os.path.join(self.project_dir, 'content', 'index.html')

        # assoziation relationship of classes, bound by json-id, so classes are bound in the same way
        self.employee = Employee(project_dir)
        self.customer = Customer(project_dir, self.employee)
        self.project = Project(project_dir, self.customer)
        self.proj_reg = Registration(project_dir, self.project)
        self.proj_hours = Hours(project_dir, self.proj_reg)

    @cherrypy.expose
    def index(self):
        with codecs.open(self.index_path, FileMode.Read.value, Encoding.UTF8.value) as file:
            return file.read()

    @cherrypy.expose
    def project_list(self):
        return self.view.create_list(self.project)

    @cherrypy.expose
    def project_form(self, key):
        return self.view.create_form(self.project, key)

    @cherrypy.expose
    def project_save(self, key, **post):
        self.project.save(key, post)
        raise cherrypy.HTTPRedirect("/project_form/" + key)

    @cherrypy.expose
    def project_add(self):
        max_key = self.project.get_max_key()
        raise cherrypy.HTTPRedirect("/project_form/" + str(max_key))

    @cherrypy.expose
    def project_del(self, key):
        self.project.delete(key)
        raise cherrypy.HTTPRedirect("/project_list/")

    @cherrypy.expose
    def customer_list(self):
        return self.view.create_list(self.customer)

    @cherrypy.expose
    def customer_form(self, key):
        return self.view.create_form(self.customer, key)

    @cherrypy.expose
    def customer_save(self, key, **post):
        self.customer.save(key, post)
        raise cherrypy.HTTPRedirect("/customer_form/" + key)

    @cherrypy.expose
    def customer_add(self):
        max_key = self.customer.get_max_key()
        raise cherrypy.HTTPRedirect("/customer_form/" + str(max_key))

    @cherrypy.expose
    def customer_del(self, key):
        self.customer.delete(key)
        raise cherrypy.HTTPRedirect("/customer_list/")

    @cherrypy.expose
    def employee_list(self):
        return self.view.create_list(self.employee)

    @cherrypy.expose
    def employee_form(self, key):
        return self.view.create_form(self.employee, key)

    @cherrypy.expose
    def employee_save(self, key, **post):
        self.employee.save(key, post)
        raise cherrypy.HTTPRedirect("/employee_form/" + key)

    @cherrypy.expose
    def employee_add(self):
        max_key = self.employee.get_max_key()
        raise cherrypy.HTTPRedirect("/employee_form/" + str(max_key))

    @cherrypy.expose
    def employee_del(self, key):
        self.employee.delete(key)
        raise cherrypy.HTTPRedirect("/employee_list/")

    @cherrypy.expose
    def registration(self, key):
        return self.view.create_form(self.proj_reg, key)

    @cherrypy.expose
    def registration_save(self, key, **post):
        self.proj_reg.save(key, post)
        return self.registration(key)

    @cherrypy.expose
    def registration_del(self, project_key, key):
        self.proj_reg.delete_employee_from_project(project_key, key)
        raise cherrypy.HTTPRedirect("/registration/" + project_key)

    @cherrypy.expose
    def hours(self, key):
        return self.view.create_form(self.proj_hours, key)

    @cherrypy.expose
    def hours_save(self, key, **post):
        self.proj_hours.save(key, post)
        raise cherrypy.HTTPRedirect("/hours/" + key)