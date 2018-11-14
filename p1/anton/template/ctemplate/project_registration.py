# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542097444.294744
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/project_registration'
_template_uri = 'project_registration'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        project_key = context.get('project_key', UNDEFINED)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Project Employee Registration</title>\n        <meta charset="UTF-8">\n        <link href="/list.css" rel="stylesheet"/>\n    </head>\n    <body>\n        <h3>Mitarbeiter hinzuf&uuml;gen</h3>\n        <form action="/registration_save/" method="post">\n            <input type="hidden" name="key" value="')
        __M_writer(str(project_key))
        __M_writer('"/>\n            <select name="id_employee">\n')
        for key in data['nonmember']:
            __M_writer('                <option value="')
            __M_writer(str(key))
            __M_writer('">')
            __M_writer(str(data['nonmember'][key]['first_name']))
            __M_writer(' ')
            __M_writer(str(data['nonmember'][key]['last_name']))
            __M_writer('</option>\n')
        __M_writer('            </select>\n            <button type="submit">Hinzuf&uuml;gen</button>\n        </form>\n        <h3>Hinzugef&uuml;gte Mitarbeiter</h3>\n        <table id="idList">\n            <tr>\n                <th>ID</th>\n                <th>Vorname</th>\n                <th>Nachname</th>\n                <th>Position</th>\n                <th>Support</th>\n                <th>Aktion</th>\n            </tr>\n')
        for key in data['member']:
            __M_writer('            <tr>\n                <td>')
            __M_writer(str(key))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data['member'][key]['first_name']))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data['member'][key]['last_name']))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data['member'][key]['position']))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data['member'][key]['support']))
            __M_writer('</td>\n                <td><a href="/registration_del/')
            __M_writer(str(project_key))
            __M_writer('/')
            __M_writer(str(key))
            __M_writer('">l&ouml;schen</a></td>\n            </tr>\n')
        __M_writer('        </table>\n        <a href="/project_list/">Zur&uuml;ck</a>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/project_registration", "uri": "project_registration", "source_encoding": "ascii", "line_map": {"16": 0, "23": 1, "24": 11, "25": 11, "26": 13, "27": 14, "28": 14, "29": 14, "30": 14, "31": 14, "32": 14, "33": 14, "34": 16, "35": 29, "36": 30, "37": 31, "38": 31, "39": 32, "40": 32, "41": 33, "42": 33, "43": 34, "44": 34, "45": 35, "46": 35, "47": 36, "48": 36, "49": 36, "50": 36, "51": 39, "57": 51}}
__M_END_METADATA
"""
