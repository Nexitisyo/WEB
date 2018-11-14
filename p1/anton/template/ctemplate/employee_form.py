# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542100461.1522114
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/employee_form'
_template_uri = 'employee_form'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Employee Formular</title>\n        <meta charset="UTF-8">\n    </head>\n    <body>\n        <form id="edit_form" action="/employee_save" method="post">\n\n            <input type="hidden" value="')
        __M_writer(str(data['employee_form']['key']))
        __M_writer('" name="key"/>\n            <p>\n                <label for="first_name">First Name: </label>\n                <input type="text" value="')
        __M_writer(str(data['employee_form']['first_name']))
        __M_writer('" id="first_name" name="first_name" required />\n            </p>\n            <p>\n                <label for="last_name">Last Name: </label>\n                <input type="text" value="')
        __M_writer(str(data['employee_form']['last_name']))
        __M_writer('" id="last_name" name="last_name" required />\n            </p>\n            <p>\n                <label for="position">Position:</label>\n                <input type="text" value="')
        __M_writer(str(data['employee_form']['position']))
        __M_writer('" id="position" name="position" required/>\n            </p>\n            <p>\n                <input type="hidden" name="support" value="off"/>\n')
        if data['employee_form']['support'] == True:
            __M_writer('                <label for="support">Support:</label><input type="checkbox" id="support" name="support" checked/>\n')
        else:
            __M_writer('                <label for="support">Support:</label><input type="checkbox" id="support" name="support"/>\n')
        __M_writer('            </p>\n\n            <input type="submit" value="Speichern" />&nbsp;\n            <a href="/employee_list">abbrechen</a>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/employee_form", "uri": "employee_form", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 10, "24": 10, "25": 13, "26": 13, "27": 17, "28": 17, "29": 21, "30": 21, "31": 25, "32": 26, "33": 27, "34": 28, "35": 30, "41": 35}}
__M_END_METADATA
"""
