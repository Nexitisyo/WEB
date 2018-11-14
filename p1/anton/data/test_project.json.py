import json
import codecs
import os
import os.path
import sys

import datetime
import time

def func(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)

def main():

    project_content = ''
    with codecs.open('project.json', 'r', 'utf-8') as file:
        project_content = json.load(file)

    customer_content = ''
    with codecs.open('customer.json', 'r', 'utf-8') as file:
        customer_content = json.load(file)

    employee_content = ''
    with codecs.open('employee.json', 'r', 'utf-8') as file:
        employee_content = json.load(file)

    for id in project_content:
        print("ID: ", id)
        print("Label: ", project_content[id]['label'])
        print("Description: ", project_content[id]['description'])

        print("Start: ", project_content[id]['processing_start'])
        print("Finish: ", project_content[id]['processing_finish'])

        print("Budget: ", project_content[id]['budget'])
        print("ID Customer: ", project_content[id]['id_customer'])

        for entry in customer_content[project_content[id]['id_customer']]:
            print(entry + ": ", customer_content[project_content[id]['id_customer']][entry])

        print("\n")

        for employee in project_content[id]['id_employee']:
            print("ID Employee: ", employee)
            print(employee_content[employee]['first_name'])
            print(employee_content[employee]['last_name'])
            print(employee_content[employee]['position'])
            #print(project_content[id]['id_employee']['last_name'])
            #print(project_content[id]['id_employee']['position'])
            for week in project_content[id]['id_employee'][employee]['week']:
                print("Week: ", week)
                print("Hours: ", project_content[id]['id_employee'][employee]['week'][week])
        print("\n")

    first_employees = dict()
    for key in project_content:
        first_employee = list(project_content[key]['id_employee'])[0]
        first_employees.update({key: first_employee})
    print("ERSTE MITARBEITER", first_employees)


    func(1, 2, 3, 4, sieben=7, acht=8)

    print(['a'] * 10)

    date_start = "2018-09-01"
    date_finish = "2018-10-01"



    date1 = datetime.date(int(date_start.split('-')[0]), int(date_start.split('-')[1]), int(date_start.split('-')[2]))
    date2 = datetime.date(int(date_finish.split('-')[0]), int(date_finish.split('-')[1]), int(date_finish.split('-')[2]))
    print(date1.strftime("%Y %m %d"))
    days_delta = date2 - date1
    print(days_delta.days)

    time.strptime(date_start.replace('-', ' '), '%Y %m %d')
    print(time.asctime())

    dict_ex = {'id_employee': ['1', '2', '3', '5']}

    dictOfWords = {i: { 'week' : { str(index) : str(index) } } for index, i in enumerate(dict_ex['id_employee'])}
    print(dictOfWords)

if __name__ == '__main__':
    main()