import copy

from .department import Department
from .customer import Customer


class Project(Department):

    def __init__(self, project_dir, customer : Customer):
        Department.__init__(self, project_dir, 'project.json')

        self.customer = customer

    def render_markup(self, key=None):
        template = None
        mako_data = {'customer': self.customer.get_data()}

        if key is not None:
            if key not in self.data:
                mako_data['project_form'] = self.get_blank_entry()
            else:
                mako_data['project_form'] = copy.deepcopy(self.data[key])

            mako_data['project_form'].update({'key': key})
            template = self.lookup.get_template('project_form')
        else:
            mako_data['project'] = self.data
            template_name = 'project_list'
            template = self.lookup.get_template('project_list')

        return template.render(data=mako_data)

    def get_customer(self):
        return self.customer

    def get_blank_entry(self):
        return {'label': '', 'description': '', 'duration': '0', 'budget': '0', 'id_customer': '', 'id_hours': []}