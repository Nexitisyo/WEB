# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540991183.3482568
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
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Web-Teams</title>\n        <meta charset="UTF-8" />\n    </head>\n    <body>\n        <table id="idList">\n            <tr>\n                <th>Matriculation Number</th>\n                <th>Forename</th>\n                <th>Surname</th>\n                <th>Session</th>\n                <th>Department</th>\n            </tr>\n')
        for key in data:
            __M_writer('            <tr>\n                <form id="form_')
            __M_writer(str(key))
            __M_writer('" action="edit" method="post">\n                    <td name="id">')
            __M_writer(str(key))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data[key]['forename']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data[key]['surname']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data[key]['session']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data[key]['department']))
            __M_writer('</td>\n                    <td>\n                        <a href="/edit">bearbeiten</a>&nbsp;\n                        <a href="/delete" class="clDelete">l&ouml;schen</a>\n                    </td>\n                </form>\n            </tr>\n')
        __M_writer('        </table>\n        <div>\n            <a href="add">erfassen</a>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/list", "uri": "list", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 16, "24": 17, "25": 18, "26": 18, "27": 19, "28": 19, "29": 20, "30": 20, "31": 21, "32": 21, "33": 22, "34": 22, "35": 23, "36": 23, "37": 31, "43": 37}}
__M_END_METADATA
"""
