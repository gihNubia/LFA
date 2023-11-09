class Transition:
    
    def __init__(self, cs, symbols, ns, nsymbols, directions):
        self.cs = cs
        self.symbols = symbols
        self.ns = ns
        self.nsymbols = nsymbols
        self.directions = directions
    
    def get_action(self, cs, symbols):
        if cs == self.cs and symbols == self.symbols:
            return self.ns, self.nsymbols, self.directions
        else:
            return None