import Piece

class Checkers:
    board = []

    def __init__(self):
        '''Initializes the board, placing the pieces on their starting squares.'''
        
        self.board = [["#" for i in range(8)] for i in range(8)]
        
        for i in range(0, 3, 2): #Row 0 and row 2
            for j in range(1, 8, 2): #Odd columns
                piece = Piece.Piece("black")
                self.board[i][j] = piece

        for i in range(0, 8, 2): #Even columns
            piece = Piece.Piece("black")
            self.board[1][i] = piece #Row 1
           
        for i in range(5, 9, 2): #Row 5 and row 7
            for j in range(0, 8, 2): #Even columns
                piece = Piece.Piece("red")
                self.board[i][j] = piece

        for i in range(1, 8, 2): #Odd columns
            piece = Piece.Piece("red")
            self.board[6][i] = piece #Row 6
    
        
    def displayBoard(self):
        '''Displays the board along with coordinate ranges from 1-8 to help visualization.'''
        for i in range(8):
            print(i+1, end=' ')
            for j in range(8):
                print(self.board[i][j], end=' ')
            print()
        
        print(" ", end=' ')
        for i in range(8):
            print(i+1, end=' ')

        print("\n")

    def makeKings(self):
        '''Promotes any pieces that have fulfilled the king requirement, that is they have reached the last rank of the opposite side'''

        for i in range(8): #Red pieces
            if (type(self.board[0][i]) == Piece.Piece and self.board[0][i].colour == "red"): #If a red piece is on the final rank, promote it
                self.board[0][i].setKing()

        for i in range(8): #Black pieces
            if (type(self.board[7][i]) == Piece.Piece and self.board[7][i].colour == "black"): #If a black piece is on the first rank, promote it
                self.board[7][i].setKing()


