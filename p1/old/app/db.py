#coding utf-8
import os
import json
import cherrypy       
        
    #json datei aufrufen
def read(dbFile): #Suche nach Json-Datei und return diese
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jsonFile = open(file=current_dir + "/../data/" + dbFile, mode='r', encoding="utf-8")
    dbJson = json.load(jsonFile)
    jsonFile.close()
    return dbJson

def updateJson(dbFile, entry): #Update json file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jsonFile = open(file=current_dir + "/../data/" + dbFile, mode='w', encoding="utf-8")
    json.dump(entry, jsonFile, indent=4)
    jsonFile.close()

def addEntry(dbFile, entry, key):
    dbJson = read(dbFile)
    for x in dbJson:    #einträge durchgehen bis key nicht vorhanden
        if x["id"] == int(key):
            entry["id"] = int(key)
            dbJson[x] = entry    #eitnrag hihnzufpgen
    updateJson(dbFile, dbJson)    #json neu schreiben/updaten

def append(dbFile, values):
    counter = read("data.json")
    counter["counter"] += 1 # Set id to lowest possible id
    values["id"] = counter["counter"]
    updateJson("data.json", counter)
    tmp = read(dbFile)
    tmp.append(values)
    updateJson(dbFile, tmp)


# def readValuebyId(dbfile, key):
#     result = read(dbfile)
#     for x in result:
#         if x["id"] == int(key):
#             return x
#     raise Exception("Eintrag nicht gefunden")

# def deleteValueById(dbfile, key):
#     result = read(dbfile)
#     for index, x in enumerate(result):
#         if x['id'] == int(key):
#             del result[index]
#     write(dbfile, result)


