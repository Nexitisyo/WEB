import os.path

from mako.lookup import TemplateLookup

from .department import Department


class View(object):

    def __init__(self, project_dir):
        self.template_dir = os.path.join(project_dir, 'template')
        self.lookup = TemplateLookup(directories=self.template_dir,
                                     module_directory=os.path.join(self.template_dir, 'ctemplate'),
                                     filesystem_checks=True)

    def create_list(self, template : Department):
        return template.render_markup()

    def create_form(self, template: Department, key):
        return template.render_markup(key)
