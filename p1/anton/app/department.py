import os.path

from abc import ABC, abstractmethod
from mako.lookup import TemplateLookup

from .database import Database


class Department(ABC):

    def __init__(self, project_dir, json_file):
        self.template_dir = os.path.join(project_dir, 'template')
        self.json_file = json_file
        self.db = Database(os.path.join(project_dir, 'data', json_file))
        self.data = self.db.read()
        self.lookup = TemplateLookup(directories=self.template_dir, module_directory=os.path.join(self.template_dir, 'ctemplate'))
        self.max_key = self.__find_new_entry_key()

    @abstractmethod
    def render_markup(self, key=None):
        pass

    @abstractmethod
    def get_blank_entry(self):
        pass

    def save(self, key: str, post: dict):
        print(post)
        if key not in self.data:
            self.data[key] = post
        else:
            self.data[key].update(post)
        self.db.write(self.data)

    def delete(self, key):
        del self.data[key]
        self.db.write(self.data)

    def get_data(self):
        return self.data

    def get_max_key(self):
        self.max_key = self.__find_new_entry_key()
        return self.max_key

    def __find_new_entry_key(self):
        new_entry_key = 0
        for key in self.data:
            new_entry_key = max(new_entry_key, int(key))

        return new_entry_key + 1