from tape import Tape
from transition import Transition

class TuringMachine:
    
    def __init__(self, word, n_tapes, initial, empty, transitions, initial_state):
        self.tapes = [Tape(initial, empty, word)]
        for _ in range(n_tapes - 1):
            self.tapes.append(Tape(initial, empty))
        
        self.transitions = []
        for t in transitions:
            cs = t[0]
            symbols = [t[2][k][0] for k in range(n_tapes)]
            ns = t[1]
            nsymbols = [t[2][k][1] for k in range(n_tapes)]
            directions = [t[2][k][2] for k in range(n_tapes)]
            self.transitions.append(Transition(cs, symbols, ns, nsymbols, directions))
        
        self.current_state = initial_state
    
    def get_next_action(self):
        cs = self.current_state
        symbols = [t.get_symbol() for t in self.tapes]
        for t in self.transitions:
            action = t.get_action(cs, symbols)
            if action is not None:
                return action
            
        return None
    
    def simulate(self):
        while True:
            action = self.get_next_action()
            if action is None:
                return self.current_state
            ns, nsymbols, directions = action
            for tape, nsymbol, direction in zip(self.tapes, nsymbols, directions):
                tape.update_symbol(nsymbol)
                tape.update_position(direction)
            self.current_state = ns