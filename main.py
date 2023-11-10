import sys
import json

from turing_machine import TuringMachine

jsonFile = sys.argv[1]
try:
    tapeContent = sys.argv[2]
except:
    tapeContent = ""

try:
    with open (jsonFile, "r") as file_object:
        jsonContent = json.load(file_object)
        mt = jsonContent["mt"]
        word = tapeContent
        n_tapes = mt[0]
        initial = mt[4]
        empty = mt[5]
        transitions = mt[6]
        initial_state = mt[7]
        
        tur_machine = TuringMachine(word, n_tapes, initial, empty, transitions, initial_state)
        if tur_machine.simulate() in mt[8]:
            print("Sim")
        else:
            print("Não")
except Exception:
    pass
