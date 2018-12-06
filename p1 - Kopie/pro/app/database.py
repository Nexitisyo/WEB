# coding: utf-8
import os
import json
import datetime

def read(dbfile):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jsonobject = open(file=current_dir + "/../data/" + dbfile, mode='r', encoding="utf-8")
    result = json.load(jsonobject)
    jsonobject.close()
    return result

def calc(start, end):

    splitStart = start.split("-")
    splitEnd = end.split("-")

    ss1 = int(splitStart[0])
    ss2 = int(splitStart[1])
    ss3 = int(splitStart[2])

    se1 = int(splitEnd[0])
    se2 = int(splitEnd[1])
    se3 = int(splitEnd[2])

    startDate = datetime.date(ss1,ss2,ss3)
    endDate = datetime.date(se1,se2,se3)

    differenceInDays = (endDate - startDate).days
    return differenceInDays
  

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
    for index, x in enumerate(result): 
        if x["id"] == int(key):
            newdata["id"] = int(key)
            result[index] = newdata
    write(dbfile, result)

def deleteValueById(dbfile, key):
    #Erweitern sodass keyLists auch gelöscht werden können
    result = read(dbfile)
    if len(key) <= 1:
        for index, x in enumerate(result):
            if x['id'] == int(key[0]):
                del result[index]
        write(dbfile, result)
    else:
        for index, x in enumerate(key):
            for index2, y in enumerate(result):
                if y['id'] == int(key[index]):
                    del result[index2]
        write(dbfile, result)           


def append(dbfile, values): 
    if dbfile == "orga.json":
        counter = read("data.json")
        values["id"] = counter["counter"]
        write("data.json", counter)
        tmp = read(dbfile)
        tmp.append(values)
        write(dbfile, tmp)
    else:
        counter = read("data.json")
        counter["counter"] += 1 # Set id to lowest possible id
        values["id"] = counter["counter"]
        write("data.json", counter)
        tmp = read(dbfile)
        tmp.append(values)
        write(dbfile, tmp)
