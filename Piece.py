class Piece:

    def __init__(self, colour):
        '''Initializes a piece based on a colour and assigns it an appropriate symbol.'''
        self.colour = colour
        self.king = False

        if self.colour == "red":
            self.symbol = "R" #Red piece
        else:
            self.symbol = "B" #Black piece
    
    def setKing(self):
        '''Sets a piece's king status, allowing it to move backwards.'''
        self.king = True
    
    def __str__(self):
        '''String representation of a piece.'''
        if (self.king == True):
            if (self.colour == "red"):
                return "K"
            else:
                return "Q" #Black kings are Q for Queen to not mess up the indentation of the board
        else:
            return self.symbol