# *************************#
# *** github  @alopezmb ***#
# *************************#

# Latest update 09 oct 2018


import json
from pathlib import Path


def formatjson(inputfilename, outputfilename):
    with open(inputfilename, "r", encoding="utf-8") as inputdata:
        with open(outputfilename, "w", encoding="utf-8") as outputdata:
            document = json.load(inputdata)
            counter = len(document)
            json.dump(document, outputdata, ensure_ascii=False, indent=4)
            return counter


# script  runs
print("  _________________________________________________________________________________________ ")
print(" |                                                                                         |  ")
print(" | Py script to clean unicode escaped chars made by Scrapy and format it into pretty output| ")
print(" |                                                                                         | ")
print(" |              ****** alejandro lopez  github @alopezmb  ******                           | ")
print(" |_________________________________________________________________________________________| ")
print("                                                                                             ")

inputfile = input("--> Input file(.json) :  ")
while not Path(inputfile).exists():
    print("File not found in current directory. Please try again : ")
    print("")
    inputfile = input("--> Input file(.json) :  ")

outputfile = input("--> Output file (.json .txt .jl) :  ")
ending = str(outputfile.split('.')[1])

while ((ending != "json") and (ending != "txt") and (ending != "jl")) or (inputfile == outputfile):
    if inputfile == outputfile:
        print("Cannot name output file the same as the input file, try again.")
        outputfile = input("--> Output file (.json .txt .jl) :  ")
        break

    print("ERROR. Output file needs to  be one of the following:  .txt , .json , .jl")
    print("Please rename OUTPUT file correctly. ")
    outputfile = input("--> Output file (.json .txt .jl) :  ")
    ending = outputfile.split('.')[1]

count = formatjson(inputfile, outputfile)
print("100% pretty printed : ** '{}' to ---> '{}'".format(inputfile, outputfile))
print("Number of entries in file: {} ".format(count))
