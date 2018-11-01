# coding: utf-8

import os
import os.path
import codecs

import json

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

   # da es hier nur darum geht, die Daten dauerhaft zu speichern,
   # wird ein sehr einfacher Ansatz verwendet:
   # - es können Daten zu genau 15 Teams gespeichert werden
   # - je Team werden 2 Teilnehmer mit Namen, Vornamen und Matrikelnummer
   #   berücksichtigt
   # - die Daten werden als eine JSON-Datei abgelegt

   #-------------------------------------------------------
   def __init__(self, workingDir_spl):
   #-------------------------------------------------------
      self.workingDir_s = workingDir_spl
      self.data_o       = None
      self.maxId_i      = None
      self.readData_p()
      self.getMaxId_p()

   #-------------------------------------------------------
   def create_px(self, data_opl):
   #-------------------------------------------------------
      # Überprüfung der Daten müsste ergänzt werden!

      # 'freien' Platz suchen,
      # falls vorhanden: belegen und Nummer des Platzes als Id zurückgeben

      self.maxId_i += 1
      id_s = str(self.maxId_i)
      self.data_o[id_s] = data_opl
      self.saveData_p()

      return id_s

   #-------------------------------------------------------
   def read_px(self, id_spl = None):
   #-------------------------------------------------------
      # hier zur Vereinfachung:
      # Aufruf ohne id: alle Einträge liefern
      data_o = None
      if id_spl == None:
         data_o = self.data_o
      else:
         if id_spl in self.data_o:
            data_o = self.data_o[id_spl]

      return data_o

   #-------------------------------------------------------
   def update_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      # Überprüfung der Daten müsste ergänzt werden!
      status_b = False
      if id_spl in self.data_o:
         self.data_o[id_spl] = data_opl
         self.saveData_p()
         status_b = True

      return status_b

   #-------------------------------------------------------
   def delete_px(self, id_spl):
   #-------------------------------------------------------
      status_b = False
      if id_spl in self.data_o:
         del self.data_o[id_spl]
         self.saveData_p()
         status_b = True

      return status_b

   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------
      return ['', '', '', '', '', '']
   
   #-------------------------------------------------------
   def readData_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open(os.path.join(self.workingDir_s, 'data', 'webteams.json'), 'r', 'utf-8')
      except:
         # Datei neu anlegen
         self.data_o = {}
         self.saveData_p()
      else:
         with fp_o:
            self.data_o = json.load(fp_o)

      return

   #-------------------------------------------------------
   def saveData_p(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join(self.workingDir_s, 'data', 'webteams.json'), 'w', 'utf-8') as fp_o:
         json.dump(self.data_o, fp_o, indent=3)


   #-------------------------------------------------------
   def getMaxId_p(self):
   #-------------------------------------------------------
      key_i = 0
      for key_s in self.data_o:
         if int(key_s) > key_i:
            key_i = int(key_s)
            
      self.maxId_i = key_i
      
# EOF
