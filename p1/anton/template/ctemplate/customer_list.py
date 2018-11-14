# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542100438.564009
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/customer_list'
_template_uri = 'customer_list'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Customer Table Content</title>\n        <meta charset="UTF-8" />\n        <link href="/list.css" rel="stylesheet"/>\n    </head>\n    <body>\n        <table id="idList">\n            <tr>\n                <th>ID</th>\n                <th>Name</th>\n                <th>Kontakt-Person</th>\n                <th>Ort</th>\n                <th>Aktion</th>\n            </tr>\n')
        for key in data['customer']:
            __M_writer('                <tr>\n                    <td>')
            __M_writer(str(key))
            __M_writer('</td>\n                    <td>')
            __M_writer(str(data['customer'][key]['label']))
            __M_writer('</td>\n                    <td>\n')
            for support_key in data['support_employee']:
                if support_key == data['customer'][key]['id_contact']:
                    __M_writer('                                ')
                    __M_writer(str(data['support_employee'][support_key]['first_name']))
                    __M_writer(' ')
                    __M_writer(str(data['support_employee'][support_key]['last_name']))
                    __M_writer('\n                                ')
                    break 
                    
                    __M_writer('\n')
            __M_writer('                    </td>\n                    <td>')
            __M_writer(str(data['customer'][key]['location']))
            __M_writer('</td>\n                    <td>\n                        <a href="/customer_form/')
            __M_writer(str(key))
            __M_writer('">bearbeiten</a>&nbsp;\n                        <a href="/customer_del/')
            __M_writer(str(key))
            __M_writer('">l&ouml;schen</a>\n                    </td>\n                </tr>\n')
        __M_writer('        </table>\n        <div>\n            <a href="/customer_add">Neuen Datensatz hinzuf&uuml;gen</a>\n            <a href="/">Zur&uuml;ck</a>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/customer_list", "uri": "customer_list", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 17, "24": 18, "25": 19, "26": 19, "27": 20, "28": 20, "29": 22, "30": 23, "31": 24, "32": 24, "33": 24, "34": 24, "35": 24, "36": 25, "38": 25, "39": 28, "40": 29, "41": 29, "42": 31, "43": 31, "44": 32, "45": 32, "46": 36, "52": 46}}
__M_END_METADATA
"""
