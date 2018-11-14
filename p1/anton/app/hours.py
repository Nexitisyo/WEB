from .department import Department
from .registration import Registration


class Hours(Department):

    def __init__(self, project_dir, registration: Registration):
        Department.__init__(self, project_dir, 'hours.json')
        self.registration = registration
        self.project = self.registration.get_project()
        self.customer = self.project.get_customer()
        self.employee = self.customer.get_employee()

        self.project_data = self.project.get_data()
        self.customer_data = self.customer.get_data()
        self.employee_data = self.employee.get_data()

        self.data = registration.get_data()
        self.project_hours = None

    def render_markup(self, project_key=None):

        self.registration.update_project_weeks(project_key)
        self.project_hours = self.get_hour_entries_of(project_key)
        mako_data = {'project_hours' : self.project_hours, 'employee' : self.employee_data}

        template = self.lookup.get_template('project_hours')
        return template.render(project_key=project_key,
                               duration=self.project_data[project_key]['duration'],
                               data=mako_data)

    def save(self, project_key: str, post: dict):
        duration = int(self.project_data[project_key]['duration'])
        for key in self.project_hours:
            for week in range(0, duration):
                self.project_hours[key]['week'][week] = post[self.project_hours[key]['id_employee']][week]
        self.data.update(self.project_hours)
        self.db.write(self.data)

    def get_blank_entry(self):
        return {'id_employee': '', 'id_project': '', 'week': []}

    def get_hour_entries_of(self, project_key):
        entries = {}
        for key in self.data:
            if self.data[key]['id_project'] == project_key:
                entries[key] = self.data[key]
        return entries
