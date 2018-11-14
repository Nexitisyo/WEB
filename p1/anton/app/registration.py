import copy

from .department import Department
from .project import Project


class Registration(Department):

    def __init__(self, project_dir, project: Project):
        Department.__init__(self, project_dir, 'hours.json')
        self.project = project
        self.customer = self.project.get_customer()
        self.employee = self.customer.get_employee()

        self.project_data = self.project.get_data()
        self.customer_data = self.customer.get_data()
        self.employee_data = self.employee.get_data()

    def render_markup(self, project_key=None):
        self.update_project_weeks(project_key)
        mako_data = {'member':    self.get_project_members(project_key),
                     'nonmember': self.get_project_nonmembers(project_key)}

        template = self.lookup.get_template('project_registration')
        return template.render(project_key=project_key, data=mako_data)

    def save(self, project_key: str, post: dict):

        max_key = self.get_max_key()

        entry = self.get_blank_entry()
        entry['id_project'] = project_key
        entry['id_employee'] = post['id_employee']
        entry['week'] = self.get_blank_week(self.project_data[project_key]['duration'])
        self.data[max_key] = entry

        self.db.write(self.data)

    def get_project_members(self, project_key):
        employees = {}
        for key in self.data:
            if self.data[key]['id_project'] == project_key:
                employees[self.data[key]['id_employee']] = self.employee_data[self.data[key]['id_employee']]

        return employees

    def get_project_nonmembers(self, project_key):
        employees = copy.deepcopy(self.employee_data)
        for key in self.data:
            if self.data[key]['id_project'] == project_key:
                del employees[self.data[key]['id_employee']]

        return employees

    def get_project(self):
        return self.project

    def delete_employee_from_project(self, project_key, employee_key):
        print(employee_key)
        for key in self.data:
            if self.data[key]['id_employee'] == employee_key and self.data[key]['id_project'] == project_key:
                super().delete(key)
                break

    #TODO: mega kompliziert, einfacheren Weg finden
    def update_project_weeks(self, project_key):
        '''passt die Anzahl der Wochen an die Dauer des Projekts und füllt evtl mit Nullen aus oder schneidet ab'''
        project_hour_entries = self.get_hour_entries_of(project_key)
        duration = int(self.project_data[project_key]['duration'])
        tmp_week = []
        for key in project_hour_entries:
            self.copy_weeks_until(project_hour_entries[key], tmp_week, min(duration, len(project_hour_entries[key]['week'])))
            if duration > len(tmp_week):
                tmp_week.extend(self.get_blank_week(duration - len(tmp_week)))
            self.data[key]['week'] = copy.deepcopy(tmp_week)
            tmp_week = []
        self.db.write(self.data)

    def copy_weeks_until(self, project_hour_entry: dict, dst_week: list, week_number: int):
        for index in range(0, week_number):
            dst_week.append(project_hour_entry['week'][index])

    def get_hour_entries_of(self, project_key):
        entries = {}
        for key in self.data:
            if self.data[key]['id_project'] == project_key:
                entries[key] = copy.deepcopy(self.data[key])
        return entries

    def get_blank_entry(self):
        return {'id_employee': '', 'id_project': '', 'week': []}

    def get_blank_week(self, duration):
        return ['0'] * int(duration)