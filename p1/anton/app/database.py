import os
import codecs
import json

from enum import Enum

class FileMode(Enum):
    Read = 'r'
    Write = 'w'


class Encoding(Enum):
    UTF8 = "utf-8"


class Database(object):

    def __init__(self, file_path):
        self.path = file_path
        self.__check_file()

    def read(self):
        with codecs.open(self.path, FileMode.Read.value, Encoding.UTF8.value) as file:
            return json.load(file)

    def write(self, data):
        with codecs.open(self.path, FileMode.Write.value, Encoding.UTF8.value) as file:
            json.dump(data, file, indent=3)

    def get_keys(self, data):
        keys = []
        for key in data:
            keys.append(key)
        return keys

    def __check_file(self):

        if self.path != '':
            if os.path.isfile(self.path) and os.stat(self.path).st_size == 0:
                with codecs.open(self.path, FileMode.Write.value, Encoding.UTF8.value) as file:
                    file.write("{}")
        else:
            raise FileNotFoundError('Path Error: ' + self.path)