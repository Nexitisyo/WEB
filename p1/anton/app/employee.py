import copy

from .department import Department


class Employee(Department):

    def get_blank_entry(self):
        return {'first_name': '', 'last_name': '', 'position': '', 'support': False}

    def __init__(self, project_dir):
        Department.__init__(self, project_dir, 'employee.json')

    def save(self, key : str, post : dict):
        # value contains a list of 2 elements if true (see: hidden element, same name)
        if post['support'] == 'off':
            post['support'] = False
        else:
            post['support'] = True

        super().save(key, post)

    def render_markup(self, key=None):
        template = None
        mako_data = {}

        if key is not None:
            if key not in self.data:
                mako_data['employee_form'] = self.get_blank_entry()
            else:
                mako_data['employee_form'] = copy.deepcopy(self.data[key])

            mako_data['employee_form'].update({'key': key})
            template = self.lookup.get_template('employee_form')
        else:
            mako_data['employee'] = self.data
            template = self.lookup.get_template('employee_list')

        return template.render(data=mako_data)

    def supporters(self):
        supporters = {}
        for key in self.data:
            if self.data[key]['support'] == True:
                supporters[key] = self.data[key]
        return supporters

    def workers(self):
        workers = {}
        for key in self.data:
            if self.data[key]['support'] == False:
                workers[key] = self.data[key]
        return workers