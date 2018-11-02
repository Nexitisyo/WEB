# coding: utf-8
import os
import json


def read(dbfile):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jsonobject = open(file=current_dir + "/../data/" + dbfile, mode='r', encoding="utf-8")
    result = json.load(jsonobject)
    jsonobject.close()
    return result


def readValuebyId(dbfile, key):
    result = read(dbfile)
    for x in result:
        if x["id"] == int(key):
            return x
    raise Exception("Eintrag nicht gefunden")


def write(dbfile, newdata): #Update json file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jsonobject = open(file=current_dir + "/../data/" + dbfile, mode='w', encoding="utf-8")
    json.dump(newdata, jsonobject, indent=4)
    jsonobject.close()
    

def writeValuebyId(dbfile, key, newdata):
    result = read(dbfile)
    # enum macht aus liste eine key value map
    for index, x in enumerate(result): # Fragen wie diese for loop in Python funktioniert && Mappen wir index UND x mit einem Eintrag aus 'result'?
        if x["id"] == int(key):
            newdata["id"] = int(key)
            result[index] = newdata # Wieso result[index] und nicht result[x]? Ist das nicht dasselbe?
    write(dbfile, result)


def deleteValueById(dbfile, key):
    result = read(dbfile)
    for index, x in enumerate(result):
        if x['id'] == int(key):
            del result[index]
    write(dbfile, result)


def append(dbfile, values): #Wofür ist das ?
    counter = read("data.json")
    counter["counter"] += 1 # Set id to lowest possible id
    values["id"] = counter["counter"]
    write("data.json", counter)
    tmp = read(dbfile)
    tmp.append(values)
    write(dbfile, tmp)
