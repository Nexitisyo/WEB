# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541084897.1932414
_enable_loop = True
_template_filename = 'C:/WEB/anton/pro/template/form'
_template_uri = 'form'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        keys = context.get('keys', UNDEFINED)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Web-Teams</title>\n        <meta charset="UTF-8">\n    </head>\n    <body>\n\n        <form id="edit_form" action="/save" method="post">\n            <div>\n')
        if keys != []:
            __M_writer('                    <label for="matriculation">Matrikelnummer</label>\n                    <input readonly pattern=".{0}|.{7,8}" list="matriculation numbers" type="number" value="')
            __M_writer(str(data["matriculation"]))
            __M_writer('" id="matriculation" name="matriculation" required  title="Either 0 chars for automatically generated or 7 to 8 chars" maxlength="8"/>\n                    <datalist id="matriculation numbers">\n')
            for key in keys:
                __M_writer('                        <option value="')
                __M_writer(str(key))
                __M_writer('">\n')
            __M_writer('                    </datalist>\n')
        __M_writer('            </div>\n            <div>\n                <label for="first_name">Vorname</label>\n                <input type="text" value="')
        __M_writer(str(data["first_name"]))
        __M_writer('" id="first_name" name="first_name" required />\n            </div>\n            <div>\n                <label for="last_name">Nachname</label>\n                <input type="text" value="')
        __M_writer(str(data["last_name"]))
        __M_writer('" id="last_name" name="last_name" required />\n            </div>\n            <div>\n                <label for="session">Session</label>\n                <input type="number" value="')
        __M_writer(str(data["session"]))
        __M_writer('" id="session" name="session" required min="1" max="99"/>\n            </div>\n            <div>\n                <label for="department">Department</label>\n                <input type="number" value="')
        __M_writer(str(data["department"]))
        __M_writer('" id="department" name="department" required min="1" max="12"/>\n            </div>\n            <div>\n                <input type="submit" value="Speichern" />&nbsp;\n                <a href="/">abbrechen</a>\n            </div>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/WEB/anton/pro/template/form", "uri": "form", "source_encoding": "ascii", "line_map": {"16": 0, "23": 1, "24": 11, "25": 12, "26": 13, "27": 13, "28": 15, "29": 16, "30": 16, "31": 16, "32": 18, "33": 20, "34": 23, "35": 23, "36": 27, "37": 27, "38": 31, "39": 31, "40": 35, "41": 35, "47": 41}}
__M_END_METADATA
"""
