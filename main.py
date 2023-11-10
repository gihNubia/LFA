import sys
import json

#nomeArq = sys.argv
jsonFile = sys.argv[1]
tapeContent = sys.argv[2]

try:
    with open (jsonFile, "r") as file_object:
        jsonContent = json.load(file_object)
except FileNotFoundError as error:
    print(error)
except json.JSONDecodeError as error2:
    print(error2)


