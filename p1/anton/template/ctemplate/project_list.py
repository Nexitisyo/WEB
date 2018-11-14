# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542096261.7679505
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/project_list'
_template_uri = 'project_list'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Project Table Content</title>\n        <meta charset="UTF-8" />\n        <link href="/list.css" rel="stylesheet"/>\n    </head>\n    <body>\n        <table id="idList">\n            <tr>\n                <th>ID</th>\n                <th>Name</th>\n                <th>Beschreibung</th>\n                <th>Bearbeitungsdauer(Wochen)</th>\n                <th>Budget</th>\n                <th>Kunde</th>\n                <th>Aktion</th>\n            </tr>\n')
        for key in data['project']:
            __M_writer('                <tr>\n                    <td>\n                        <input type="hidden" name="keys" value="')
            __M_writer(str(key))
            __M_writer('"/>\n                        ')
            __M_writer(str(key))
            __M_writer('\n                    </td>\n                    <td>')
            __M_writer(str(data['project'][key]['label']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['project'][key]['description']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['project'][key]['duration']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['project'][key]['budget']))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['customer'][data['project'][key]['id_customer']]['label']))
            __M_writer('</td>\n                    <td>\n                        <a href="/project_form/')
            __M_writer(str(key))
            __M_writer('">bearbeiten</a>&nbsp;\n                        <a href="/project_del/')
            __M_writer(str(key))
            __M_writer('">l&ouml;schen</a>\n                        <a href="/registration/')
            __M_writer(str(key))
            __M_writer('">Mitarbeiter zuordnen</a>\n                        <a href="/hours/')
            __M_writer(str(key))
            __M_writer('">Arbeitsstunden</a>\n                    </td>\n                </tr>\n')
        __M_writer('        </table>\n        <div>\n            <a href="/project_add">Neuen Datensatz hinzuf&uuml;gen</a>\n            <a href="/">Zur&uuml;ck</a>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/project_list", "uri": "project_list", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 19, "24": 20, "25": 22, "26": 22, "27": 23, "28": 23, "29": 25, "30": 25, "31": 26, "32": 26, "33": 27, "34": 27, "35": 28, "36": 28, "37": 29, "38": 29, "39": 31, "40": 31, "41": 32, "42": 32, "43": 33, "44": 33, "45": 34, "46": 34, "47": 38, "53": 47}}
__M_END_METADATA
"""
