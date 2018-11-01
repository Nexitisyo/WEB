# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541082248.1981144
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/list'
_template_uri = 'list'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Web-Teams</title>\n        <meta charset="UTF-8" />\n        <link href="/style.css" rel="stylesheet">\n    </head>\n    <body>\n        <table id="idList">\n            <tr>\n                <th>Matriculation Number</th>\n                <th>First Name</th>\n                <th>Last Name</th>\n                <th>Session</th>\n                <th>Department</th>\n                <th>Operation</th>\n            </tr>\n')
        for key in data:
            __M_writer('            <tr>\n                <td>')
            __M_writer(str(key))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data[key]['first_name']))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data[key]['last_name']))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data[key]['session']))
            __M_writer('</td>\n                <td>')
            __M_writer(str(data[key]['department']))
            __M_writer('</td>\n                <td>\n                    <a href="/edit/')
            __M_writer(str(key))
            __M_writer('">bearbeiten</a>&nbsp;\n                    <a href="/delete/')
            __M_writer(str(key))
            __M_writer('">l&ouml;schen</a>\n                </td>\n            </tr>\n')
        __M_writer('        </table>\n        <div>\n            <a href="/add">Neuen Datensatz hinzuf&uuml;gen</a>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/list", "uri": "list", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 18, "24": 19, "25": 20, "26": 20, "27": 21, "28": 21, "29": 22, "30": 22, "31": 23, "32": 23, "33": 24, "34": 24, "35": 26, "36": 26, "37": 27, "38": 27, "39": 31, "45": 39}}
__M_END_METADATA
"""
