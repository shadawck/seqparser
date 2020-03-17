"""
usage: 
    seqparse.py list [--filepath <REGEX_FILE>]
    seqparse.py find [--all] --filepath <REGEX_FILE> --source <SOURCE_FILE> 
    seqparse.py find [--partial <REGEX_NAME>] --filepath <REGEX_FILE> --source <SOURCE_FILE> 

Options:
  -h --help         Show this screen
  --version         Show version
  -f --filepath     Add filepath
  -a --all          Search through all Regex input 
  -p --partial      Input specific expression
  -s --source       Source file to search for regex
"""

import re
import json
from docopt import docopt

###############################
######### CLI function ########
###############################

def regexListing(filepath): 
    d = listToDict(filepath)
    for item in d : 
        print(item)


def getData(filepath): 
    file = open(filepath, 'r')
    data = file.read()
    file.close()
    return data

# def get_var_module_name(module_name):
#     module = globals().get(module_name, None)
#     var = {}
#     if module:
#         var = {key: value for key, value in module.__dict__.items() if not (key.startswith('__') or key.startswith('_'))}
#     return var
# 
# def print_var_module_name(module_name):
#     regexVar = get_var_module_name(module_name)
#     for key, value in regexVar.items():
#         print("{:<30}{:<100}".format(key, value))

def listToDict(filepath): 
    with open(filepath) as fh:
        regexDict = dict(line.strip().split(' = ', 1) for line in fh)
    fh.close()

    return regexDict


def matchAll(filepath, data) : 
    d      = listToDict(filepath)
    data   = getData(data)
    result = []

    for item in d:
        print(item + ':', re.findall(d[item], data))

def matchPartial(regexName,filepath,data):
    d      = listToDict(filepath)
    data   = getData(data)
    print(regexName + ':', re.findall(d[regexName],data))



if __name__ == '__main__': 
    arguments = docopt(__doc__, version='Naval Fate 2.0')

    defaultRegex = 'regIndex.txt'

    # LIST COMMAND : List Regex Input
    if arguments["list"]: 
        if arguments["--filepath"]:
            if arguments["<REGEX_FILE>"]: 
                print(regexListing(arguments["<REGEX_FILE>"]))
            else : print(">>> Choose a regex file <<<")
        else : print(regexListing(defaultRegex))

    # FIND COMMAND: Find Regex in data source 
    if arguments["find"] & arguments["--all"]: 
            matchAll(arguments["<REGEX_FILE>"],arguments["<SOURCE_FILE>"])
        
    if arguments["find"] & arguments["--partial"]:
        if arguments["--filepath"] & arguments["--source"]:
            print(matchPartial(arguments["<REGEX_NAME>"], arguments["<REGEX_FILE>"] , arguments["<SOURCE_FILE>"]))
    

            
# add output option and feature  -> Display result in json and stdin in a nice format
# add specific analysis on some regex : Ex :  (with a --detail flag for example)
    # P2PKH which begin with the number 1, eg: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2.
    # P2SH type starting with the number 3, eg: 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy.
    # Bech32 type starting with bc1, eg: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq.