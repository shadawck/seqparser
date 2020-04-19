#!/usr/bin/env python3

"""Seqparser 1.1.1
Usage: 
    seqparser list [--filepath <REGEX_FILE>]
    seqparser find --source <SOURCE_FILE> [--filepath <REGEX_FILE>] 
    seqparser find --partial <REGEX_NAME> --source <SOURCE_FILE> [--filepath <REGEX_FILE>]

Options:
  -h --help         Show this screen
  --version         Show version
  -f --filepath     Add filepath
  -a --all          Search through all Regex input 
  -p --partial      Input specific expression
  -s --source       Source file to search for regex
"""

import os 
from docopt import docopt
from seqparser import seqparser as sp




###############################
######### CLI function ########
###############################

def regexListing(filepath): 
    d = sp.listToDict(filepath)
    for item in d : 
        print(item)

########  MAIN  #########

def main():
    arguments = docopt(__doc__, version='Seqparser 1.1.2')
    
    ###############################
    ########### CLI VAR ########### 
    ###############################
    __REGEX_FILE = arguments["<REGEX_FILE>"]
    __SOURCE_FILE = arguments["<SOURCE_FILE>"]
    __REGEX_NAME = arguments["<REGEX_NAME>"]
    
    __file = arguments["--filepath"]
    __source = arguments["--source"]
    __partial = arguments["--partial"]

    _find_ = arguments["find"]
    _list_ = arguments["list"]

    path = os.path.abspath(os.path.dirname(__file__))
    defaultRegex=  os.path.join(path, "regIndex.txt")


    # LIST COMMAND : List Regex Input
    if _list_: 
        if __file:
            if __REGEX_FILE:
                print(regexListing(__REGEX_FILE))
            else : print(">>> Choose a regex file <<<")
        else : print(regexListing(defaultRegex))

    # FIND COMMAND: Find Regex in data source 

    if _find_ : 

        # if file is True then it is set by the user else use default
        if __file == False :
            __REGEX_FILE = defaultRegex
            
        if __partial:
            sp.matchPartial(__REGEX_NAME, __REGEX_FILE , __SOURCE_FILE)
        
        else: sp.matchAll(__REGEX_FILE,__SOURCE_FILE)
        


if __name__ == '__main__': 
    main()

            
# add output option and feature  -> Display result in json and stdin in a nice format
# add specific analysis on some regex : Ex :  (with a --detail flag for example)
    # P2PKH which begin with the number 1, eg: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2.
    # P2SH type starting with the number 3, eg: 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy.
    # Bech32 type starting with bc1, eg: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq.