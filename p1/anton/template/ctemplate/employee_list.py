# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542100453.039559
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/employee_list'
_template_uri = 'employee_list'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Employee Table Content</title>\n        <meta charset="UTF-8" />\n        <link href="/list.css" rel="stylesheet"/>\n    </head>\n    <body>\n        <table id="idList">\n            <tr>\n                <th>ID</th>\n                <th>Vorname</th>\n                <th>Name</th>\n                <th>Position</th>\n                <th>Support</th>\n                <th>Aktion</th>\n            </tr>\n')
        for key in data['employee']:
            __M_writer('                <tr>\n                    <td>')
            __M_writer(str(key))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['employee'][key]['first_name']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['employee'][key]['last_name']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['employee'][key]['position']))
            __M_writer('</td>\n                    <td>\n')
            if data['employee'][key]['support'] == True:
                __M_writer('                            Yes\n')
            else:
                __M_writer('                            No\n')
            __M_writer('                    </td>\n                    <td>\n                        <a href="/employee_form/')
            __M_writer(str(key))
            __M_writer('">bearbeiten</a>&nbsp;\n                        <a href="/employee_del/')
            __M_writer(str(key))
            __M_writer('">l&ouml;schen</a>\n                    </td>\n                </tr>\n')
        __M_writer('        </table>\n        <div>\n            <a href="/employee_add">Neuen Datensatz hinzuf&uuml;gen</a>\n            <a href="/">Zur&uuml;ck</a>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/employee_list", "uri": "employee_list", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 18, "24": 19, "25": 20, "26": 20, "27": 21, "28": 21, "29": 22, "30": 22, "31": 23, "32": 23, "33": 25, "34": 26, "35": 27, "36": 28, "37": 30, "38": 32, "39": 32, "40": 33, "41": 33, "42": 37, "48": 42}}
__M_END_METADATA
"""
