import copy

from .department import Department
from .employee import Employee


class Customer(Department):


    def __init__(self, project_dir, employee : Employee):

        Department.__init__(self, project_dir, 'customer.json')
        self.employee = employee

    def render_markup(self, key=None):
        template = None
        mako_data = {'support_employee': self.employee.supporters()}

        if key != None:
            if key not in self.data:
                mako_data['customer_form'] = self.get_blank_entry()
            else:
                mako_data['customer_form'] = copy.deepcopy(self.data[key])

            mako_data['customer_form'].update({'key' : key})
            template = self.lookup.get_template('customer_form')
        else:
            mako_data['customer'] = self.data
            template = self.lookup.get_template('customer_list')

        return template.render(data=mako_data)

    def save(self, key: str, post: dict):
        print(post)
        super().save(key, post)

    def get_employee(self):
        return self.employee

    def get_blank_entry(self):
        return {'label': '', 'id_contact': '', 'location': ''}
