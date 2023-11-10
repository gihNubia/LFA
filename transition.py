class Transition:
    
    def __init__(self, cs, symbols, ns, nsymbols, directions):
        n_direction = {
            ">": 1,
            "|": 0,
            "<": -1,
            
            "I": 0
        }
        self.cs = cs
        self.symbols = symbols
        self.ns = ns
        self.nsymbols = nsymbols
        self.directions = [n_direction[d] for d in directions]
    
    
    def get_action(self, cs, symbols):
        if cs == self.cs and symbols == self.symbols:
            return self.ns, self.nsymbols, self.directions
        else:
            return None