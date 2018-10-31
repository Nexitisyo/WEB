import os.path
from mako.lookup import TemplateLookup

class CView(object):

    def __init__(self, project_dir):
        self.template_dir = os.path.join(project_dir, 'template')
        print(self.template_dir)
        self.lookup = TemplateLookup(directories=self.template_dir,
                                     module_directory=os.path.join(self.template_dir, 'ctemplate'),
                                     filesystem_checks=True)

    # TODO: Weitere Methoden
    def create(self, template_filename, data):
        template = self.lookup.get_template(template_filename)
        markup_code = template.render(data=data)
        return markup_code

    # TODO: Could be replaced?
    def create_list(self, data):
        return self.create('list', data)


    def create_form(self, id, data):
        return self.create('form', data)
