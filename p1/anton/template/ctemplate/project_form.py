# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542099573.772794
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/project_form'
_template_uri = 'project_form'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Project Formular</title>\n        <meta charset="UTF-8">\n        <link href="/project_form.css" rel="stylesheet"/>\n    </head>\n    <body>\n        <form id="edit_form" action="/project_save" method="post">\n            <input type="hidden" value="')
        __M_writer(str(data['project_form']['key']))
        __M_writer('" name="key"/>\n            <p>\n                <label for="label">Name: </label>\n                <input type="text" value="')
        __M_writer(str(data['project_form']['label']))
        __M_writer('" id="label" name="label" required />\n            </p>\n            <p>\n                <label for="description">Beschreibung: </label>\n                <input type="text" value="')
        __M_writer(str(data['project_form']['description']))
        __M_writer('" id=description" name="description" required />\n            </p>\n            <p>\n                <label for="duration">Bearbeitungsdauer(Wochen): </label>\n                <input type="number" value="')
        __M_writer(str(data['project_form']['duration']))
        __M_writer('" name="duration" min="4"/>\n            </p>\n            <p>\n                <label for="budget">Budget: </label>\n                <input type="number" value="')
        __M_writer(str(data['project_form']['budget']))
        __M_writer('" id="budget" name="budget" required/>\n            </p>\n            <p>\n                <label for="customer">Kunde: </label>\n                <select name="id_customer" id="customer">\n')
        for key in data['customer']:
            if key == data['project_form']['id_customer']:
                __M_writer('                            <option value="')
                __M_writer(str(key))
                __M_writer('" selected>')
                __M_writer(str(data['customer'][key]['label']))
                __M_writer('</option>\n')
            else:
                __M_writer('                            <option value="')
                __M_writer(str(key))
                __M_writer('">')
                __M_writer(str(data['customer'][key]['label']))
                __M_writer('</option>\n')
        __M_writer('                </select>\n            </p>\n            <input type="submit" value="Speichern" />&nbsp;\n            <a href="/project_list/">abbrechen</a>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/project_form", "uri": "project_form", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 10, "24": 10, "25": 13, "26": 13, "27": 17, "28": 17, "29": 21, "30": 21, "31": 25, "32": 25, "33": 30, "34": 31, "35": 32, "36": 32, "37": 32, "38": 32, "39": 32, "40": 33, "41": 34, "42": 34, "43": 34, "44": 34, "45": 34, "46": 37, "52": 46}}
__M_END_METADATA
"""
