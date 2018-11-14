# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542102950.009448
_enable_loop = True
_template_filename = '/home/ashkolnik/Workspace/web/p1/pro/template/customer_form'
_template_uri = 'customer_form'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        data = context.get('data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Customer Formular</title>\n        <meta charset="UTF-8">\n    </head>\n    <body>\n        <form id="edit_form" action="/customer_save" method="post">\n            <input type="hidden" value="')
        __M_writer(str(data['customer_form']['key']))
        __M_writer('" name="key"/>\n            <p>\n                <label for="label">Company: </label>\n                <input type="text" value="')
        __M_writer(str(data['customer_form']['label']))
        __M_writer('" id="label" name="label" required />\n            </p>\n            <p>\n                <label for="contact">Contact: </label>\n                <select name="id_contact" id="contact">\n')
        for key in data['support_employee']:
            if key == data['customer_form']['id_contact']:
                __M_writer('                        <option value="')
                __M_writer(str(key))
                __M_writer('" selected>')
                __M_writer(str(data['support_employee'][key]['first_name']))
                __M_writer(' ')
                __M_writer(str(data['support_employee'][key]['last_name']))
                __M_writer(' </option>\n')
            else:
                __M_writer('                        <option value="')
                __M_writer(str(key))
                __M_writer('">')
                __M_writer(str(data['support_employee'][key]['first_name']))
                __M_writer(' ')
                __M_writer(str(data['support_employee'][key]['last_name']))
                __M_writer(' </option>\n')
        __M_writer('                </select>\n            </p>\n            <p>\n                <label for="location">Location:</label>\n                <input type="text" value="')
        __M_writer(str(data['customer_form']['location']))
        __M_writer('" id="location" name="location" required/>\n            </p>\n\n            <input type="submit" value="Speichern" />&nbsp;\n            <a href="/customer_list">abbrechen</a>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ashkolnik/Workspace/web/p1/pro/template/customer_form", "uri": "customer_form", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 9, "24": 9, "25": 12, "26": 12, "27": 17, "28": 18, "29": 19, "30": 19, "31": 19, "32": 19, "33": 19, "34": 19, "35": 19, "36": 20, "37": 21, "38": 21, "39": 21, "40": 21, "41": 21, "42": 21, "43": 21, "44": 24, "45": 28, "46": 28, "52": 46}}
__M_END_METADATA
"""
