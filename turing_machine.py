class TuringMachine:
    
    # TODO: Receber parametros da TuringMachine
    def __init__():
        pass
    
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