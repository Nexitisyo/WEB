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
        # Pfad hier zur Vereinfachung fest vorgeben
        #os.path.join(path, *paths)
        self.path_s = os.path.join(path_spl, "template") # Dunno what path_spl ist aber dadurch ist path_s der Inhalt vom Ordner "template" bekannt
        self.lookup_o = TemplateLookup(directories=self.path_s)

    # ... weitere Methoden

    # -------------------------------------------------------
    def create(self, template_spl, data_opl=None):
        if data_opl == None:
            data_opl = {} # erstelle dictionary ({} = dictionary)

        # -------------------------------------------------------
        # Auswertung mit templates
        template_o = self.lookup_o.get_template(template_spl)
        # mit der Methode render wird das zuvor 'übersetzte' Template ausgeführt
        # data_o sind die im Template angegebenen Daten
        # data_opl die übergebenen Daten
        markup_s = template_o.render(**data_opl) #Herzstück, was die Templates ausführt. # Fragen how this works
        return markup_s

# EOF
