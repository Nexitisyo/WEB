# coding: utf-8
import os.path

from mako.template import Template
from mako.lookup import TemplateLookup

# ----------------------------------------------------------
class View(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self, path_spl): #Was ist path_spl? 
    # -------------------------------------------------------
        self.path_s = os.path.join(path_spl, "template") 
        self.lookup_o = TemplateLookup(directories=self.path_s)
        
    # -------------------------------------------------------
    def create(self, template_spl, data_opl=None, data2=None, data3=None):
        if data_opl == None:
            data_opl = {} # erstelle dictionary ({} = dictionary)
        if data2 == None:
            data2 = {}
        if data3 == None:
            data3 = {}

        template_o = self.lookup_o.get_template(template_spl)
        markup_s = template_o.render(**data_opl,**data2,**data3)
        return markup_s

# EOF
