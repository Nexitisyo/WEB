import os.path
from mako.lookup import TemplateLookup


class CView(object):

    def __init__(self, project_dir):
        self.template_dir = os.path.join(project_dir, 'template')
        self.lookup = TemplateLookup(directories=self.template_dir,
                                     module_directory=os.path.join(self.template_dir, 'ctemplate'),
                                     filesystem_checks=True)

    def create_list(self, data):
        template = self.lookup.get_template('list')
        print("test")
        print("DATA: " , data)
        return template.render(data=data)


    def create_form(self, id, data, keys):

        template = self.lookup.get_template('form')

        if id != None:
            data.update({"matriculation"  : id})
        else:
            data = self.empty_dataset()

        return template.render(data=data, keys=keys)

    def empty_dataset(self):
        return {"matriculation": "", "first_name": "", "last_name": "", "session": "", "department": ""}