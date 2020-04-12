import re
import json

def getData(filepath): 
    file = open(filepath, 'r')
    data = file.read()
    file.close()
    return data

def listToDict(filepath): 
    with open(filepath) as fh:
        regexDict = dict(line.strip().split(' = ', 1) for line in fh)
    fh.close()

    return regexDict


def matchAll(filepath, data) : 
    d      = listToDict(filepath)
    data   = getData(data)

    for item in d:
        print(item + ':', re.findall(d[item], data))

def matchPartial(regexName,filepath,data):
    d      = listToDict(filepath)
    data   = getData(data)
    found = re.findall(d[regexName],data)
    for f in found :
        print(regexName + ':', f)




