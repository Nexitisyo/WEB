import os
import codecs

import json

#Daten als JSON ablegen
class CDatabase(object):

    def __init__(self, project_dir):

        self.data_dir = os.path.join(project_dir, 'data')
        self.data = None
        self.last_id = None
        self.read_data()
        self.get_max_id()

    # read all entries
    def read(self, id = None):
        data = None
        if id == None:
            data = self.data
        else:
            if id in self.data:
                data = self.data[id]

        return data

    def read_data(self):
        read_mode = 'r'; file_encoding = 'utf-8'
        json_file = 'students.json'

        try:
            file = codecs.open(os.path.join(self.data_dir, json_file), read_mode, file_encoding)
        except:
            # File does not exist: create new file
            self.data = {}
            self.save_data()
            print("error: file does not exist, saving current data into new created file")
        else:
            with file:
                self.data = json.load(file)
        return

    def save_data(self):
        write_mode = 'w'; file_encoding = 'utf-8'
        json_file = 'students.json'

        with codecs.open(os.path.join(self.data_dir, json_file), write_mode, file_encoding) as file:
            json.dump(self.data, file, indent=3)

    def get_max_id(self):
        '''Calculates Max-ID Tupel'''
        key_index = 0
        for key in self.data:
            if int(key) > key_index:
                key_index = int(key)
        self.last_id = key_index

    def create(self, json_data):
        #TODO überprüfen der Daten muss ergänzt werden

        self.last_id += 1
        id = str(self.last_id)
        self.data[id] = json_data
        self.save_data()

        return id

    def update(self, id, json_data):
        status = False
        if id in self.data:
            del self.data[id]
            self.save_data()
            status = True

        return status

    def delete(self, id):
        status = False
        if id in self.data:
            del self.data[id]
            self.save_data()
            status = True

        return status