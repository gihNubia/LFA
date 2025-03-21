class Tape:
    
    def __init__(self, initial, empty, word = None):
        self.initial = initial
        self.empty = empty
        self.currentPosition = 1
        if word is None:
            self.content = [initial, empty]
        else:
            self.content = [initial] + list(word)
            if len(self.content) == 1:
                self.content.append(empty)
    
    def update_symbol(self, newSymbol):
        self.content[self.currentPosition] = newSymbol
    
    def get_symbol(self):
        return self.content[self.currentPosition]
    
    # -1 left, 0 stay, 1 right
    def update_position(self, direction):
        self.currentPosition += direction
        if self.currentPosition >= len(self.content):
            self.content.append(self.empty)