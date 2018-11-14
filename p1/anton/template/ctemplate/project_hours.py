# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542099567.6960557
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/project_hours'
_template_uri = 'project_hours'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loop = __M_loop = runtime.LoopStack()
        project_key = context.get('project_key', UNDEFINED)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Project Formular</title>\n        <meta charset="UTF-8">\n        <link href="/project_form.css" rel="stylesheet"/>\n    </head>\n    <body>\n        <h3>Stunden-Aufwand zuweisen</h3>\n        <form id="edit_form" action="/hours_save" method="post">\n            <input type="hidden" value="')
        __M_writer(str(project_key))
        __M_writer('" name="key"/>\n')
        loop = __M_loop._enter(data['project_hours'])
        try:
            for key in loop:
                __M_writer('                <input type="hidden" name="id_employee" value="')
                __M_writer(str(data['project_hours'][key]['id_employee']))
                __M_writer('"/>\n                ')
                __M_writer(str(data['employee'][data['project_hours'][key]['id_employee']]['first_name']))
                __M_writer('\n                ')
                __M_writer(str(data['employee'][data['project_hours'][key]['id_employee']]['last_name']))
                __M_writer('\n                <div class="week_box">\n')
                loop = __M_loop._enter(data['project_hours'][key]['week'])
                try:
                    for value in loop:
                        __M_writer('                    <label for="week_')
                        __M_writer(str(loop.index))
                        __M_writer('">')
                        __M_writer(str(loop.index + 1))
                        __M_writer('. Week:</label>\n                    <input type="number" id="week_')
                        __M_writer(str(loop.index + 1))
                        __M_writer('" name="')
                        __M_writer(str(data['project_hours'][key]['id_employee']))
                        __M_writer('" value="')
                        __M_writer(str(value))
                        __M_writer('" min="0"/>\n                    </br>\n')
                finally:
                    loop = __M_loop._exit()
                __M_writer('                </div>\n')
        finally:
            loop = __M_loop._exit()
        __M_writer('            </table>\n            <input type="submit" value="Speichern"/>&nbsp;\n            <a href="/project_list/">Zur&uuml;ck</a>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/project_hours", "uri": "project_hours", "source_encoding": "ascii", "line_map": {"16": 0, "24": 1, "25": 11, "26": 11, "27": 12, "30": 13, "31": 13, "32": 13, "33": 14, "34": 14, "35": 15, "36": 15, "37": 17, "40": 18, "41": 18, "42": 18, "43": 18, "44": 18, "45": 19, "46": 19, "47": 19, "48": 19, "49": 19, "50": 19, "53": 22, "56": 24, "62": 56}}
__M_END_METADATA
"""
