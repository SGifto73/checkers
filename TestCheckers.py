import Checkers, Piece, random
checkers = Checkers.Checkers()
turn = True #Starts on human turn
redWin = False
blackWin = False #Win conditions

def isValidMove(board, startX, startY, endX, endY):
    '''Checks valid moves by comparing the start and end coordinates as well as if the spaces are occupied'''
    if board.board[startX][startY].colour == "red": #Human piece moving
        if(board.board[startX][startY].king): #Slightly different logic for kings encompasses all 4 directions
            
            if (type(board.board[endX][endY]) == str): #Empty space
                return (((startX - endX == 1) or (startX - endX == -1)) and ((endY - startY == -1) or (endY - startY == 1))) #Checks both upwards and downwards as kings can do both
            else: #Error occured, space already taken
                return False

        else:
            if (type(board.board[endX][endY]) == str): #Empty space
                return ((startX - endX == 1) and ((endY - startY == -1) or (endY - startY == 1))) #Only checks upwards
            else: #Error occured, space already taken
                return False

    else:
        if ((endX <= 7 and endX >= 0) and (endY <= 7 and endY >= 0) and board.board[endX][endY] == '#'): #Simpler code for AI, just check if the end coordinates are valid and the space is empty
            return True
        else:
            return False

def isValidJump(board, startX, startY, endX, endY):
    '''Checks valid jumps first by making sure there is an enemy piece between the two squares and then making sure the end square is empty'''
    if board.board[startX][startY].colour == "red": #Human piece moving
        if(board.board[startX][startY].king): #Slightly different logic for kings encompasses all 4 directions
            if (type(board.board[endX][endY]) == str): #Empty space
                if (startX - endX == 2): #Upwards jump
                    if (startY - endY == -2): #Rightward jump
                        if(type(board.board[startX-1][startY+1]) == Piece.Piece and board.board[startX-1][startY+1].colour == "black"): #If it's an enemy piece it can be jumped
                            return True
                        else: #Not a piece that can be jumped
                            return False
                    elif (startY - endY == 2): #Leftward jump
                        return(type(board.board[startX-1][startY-1]) == Piece.Piece and board.board[startX-1][startY-1].colour == "black")
                    else: #Invalid Y coordinate
                        return False
                elif (startX - endX == -2): #Downwards jump
                    if (startY - endY == -2): #Rightward jump
                        if(type(board.board[startX+1][startY+1]) == Piece.Piece and board.board[startX+1][startY+1].colour == "black"): #If it's an enemy piece it can be jumped
                            return True
                        else: #Not a piece that can be jumped
                            return False
                    elif (startY - endY == 2): #Leftward jump
                        return(type(board.board[startX+1][startY-1]) == Piece.Piece and board.board[startX+1][startY-1].colour == "black")
                    else: #Invalid Y coordinate
                        return False
                else: #Invalid X coordinate 
                    return False
            else: #Error occured, space already taken
                return False
    
        else:
            if (type(board.board[endX][endY]) == str): #Empty space
                if (startX - endX == 2):
                    if (startY - endY == -2): #Rightward jump
                        if(type(board.board[startX-1][startY+1]) == Piece.Piece and board.board[startX-1][startY+1].colour == "black"): #If it's an enemy piece it can be jumped
                            return True
                        else: #Not a piece that can be jumped
                            return False
                    elif (startY - endY == 2): #Leftward jump
                        return(type(board.board[startX-1][startY-1]) == Piece.Piece and board.board[startX-1][startY-1].colour == "black")
                    else: #Invalid Y coordinate
                        return False
                else: #Not an upward move or otherwise invalid X coordinate 
                    return False
            else: #Error occured, space already taken
                return False
    else:
        if ((endX <= 7 and endX >= 0) and (endY <= 7 and endY >= 0)): #Make sure coordinates in range
            if(board.board[startX][startY].king): #Slightly different logic for kings encompasses all 4 directions
                if (type(board.board[endX][endY]) == str): #Empty space
                    if (startX - endX == 2): #Upwards jump
                        if (startY - endY == -2): #Rightward jump
                            if(type(board.board[startX-1][startY+1]) == Piece.Piece and board.board[startX-1][startY+1].colour == "red"): #If it's an enemy piece it can be jumped
                                return True
                            else: #Not a piece that can be jumped
                                return False
                        elif (startY - endY == 2): #Leftward jump
                            return(type(board.board[startX-1][startY-1]) == Piece.Piece and board.board[startX-1][startY-1].colour == "red")
                        else: #Invalid Y coordinate
                            return False
                    elif (startX - endX == -2): #Downwards jump
                        if (startY - endY == -2): #Rightward jump
                            if(type(board.board[startX+1][startY+1]) == Piece.Piece and board.board[startX+1][startY+1].colour == "red"): #If it's an enemy piece it can be jumped
                                return True
                            else: #Not a piece that can be jumped
                                return False
                        elif (startY - endY == 2): #Leftward jump
                            return(type(board.board[startX+1][startY-1]) == Piece.Piece and board.board[startX+1][startY-1].colour == "red")
                        else: #Invalid Y coordinate
                            return False
                    else: #Invalid X coordinate 
                        return False
                else: #Error occured, space already taken
                    return False
        
            else:
                if (type(board.board[endX][endY]) == str): #Empty space
                    if (startX - endX == -2):
                        if (startY - endY == -2): #Rightward jump
                            if(type(board.board[startX+1][startY+1]) == Piece.Piece and board.board[startX+1][startY+1].colour == "red"): #If it's an enemy piece it can be jumped
                                return True
                            else: #Not a piece that can be jumped
                                return False
                        elif (startY - endY == 2): #Leftward jump
                            return(type(board.board[startX+1][startY-1]) == Piece.Piece and board.board[startX+1][startY-1].colour == "red")
                        else: #Invalid Y coordinate
                            return False
                    else: #Not a downwards move or otherwise invalid X coordinate 
                        return False
                else: #Error occured, space already taken
                    return False
        else:
            return False


def generateFalseBoard():
    '''Function that generates a copy of the board to be modified and then scrapped without worry of altering the game state.'''
    falseBoard = Checkers.Checkers()
    falseBoard.board = [["#" for i in range(8)] for i in range(8)]

    for i in range (8):
        for j in range(8):
            falseBoard.board[i][j] = checkers.board[i][j]
    return falseBoard

def judge(board):
    '''Judges the score of a board based on piece advantage number of threats, number of attacks, and number of kings for the AI.'''
    score = 0

    #First factor - Piece Advantage and Number of Kings
    redCount = 0
    blackCount = 0

    for line in board.board:
        for item in line:
            if(type(item) == Piece.Piece):
                if(item.colour == "red"):
                    redCount += 1
                    if (item.king):
                        redCount += 1 #Kings get additional points
                else:
                    blackCount += 1
                    if (item.king):
                        blackCount +=1
    
    score += (blackCount - redCount) * 2 #Multiplied by two because having more pieces should be weighed highly

    #Second factor - Number of threats
    threats = 0

    for i in range(8):
        for j in range(8):
            if (type(board.board[i][j]) == Piece.Piece and board.board[i][j].colour == "black"): 
                #For every black piece check the surrounding squares for threats
                if (i+1 <= 7 and j+1 <= 7 and i-1 >= 0 and j-1 >= 0 and type(board.board[i+1][j+1]) == Piece.Piece and board.board[i+1][j+1].colour == "red" and board.board[i-1][j-1] == '#'):
                    #The above if statement determines whether the square to the bottom right contains an enemy piece who can jump to the top left, which would capture this piece
                    threats += 1
                elif (i+1 <= 7 and j+1 <= 7 and i-1 >= 0 and j-1 >= 0 and type(board.board[i+1][j-1]) == Piece.Piece and board.board[i+1][j-1].colour == "red" and board.board[i-1][j+1] == '#'):
                    threats += 1

                    #Repeat two more times for king captures
                elif (i+1 <= 7 and j+1 <= 7 and i-1 >= 0 and j-1 >= 0 and type(board.board[i-1][j+1]) == Piece.Piece and board.board[i-1][j+1].colour == "red" and board.board[i+1][j-1] == '#'):
                    threats += 1
                elif (i+1 <= 7 and j+1 <= 7 and i-1 >= 0 and j-1 >= 0 and type(board.board[i-1][j-1]) == Piece.Piece and board.board[i-1][j-1].colour == "red" and board.board[i+1][j+1] == '#'):
                    threats += 1
    #The end result of the loop is the number of threats
    score -= threats*0.5

    #Third factor - Number of attacks
    attacks = 0

    #Test all jumps for attacks
    for i in range(8):
        for j in range(8):
            if (type(board.board[i][j]) == Piece.Piece and board.board[i][j].colour == "black"):
                if(board.board[i][j].king):
                    if(isValidJump(board, i, j, i+2, j+2)):
                        attacks += 1
                    if(isValidJump(board, i, j, i+2, j-2)):
                        attacks += 1
                    if(isValidJump(board, i, j, i-2, j+2)):
                        attacks += 1
                    if(isValidJump(board, i, j, i-2, j-2)):
                        attacks += 1
                else:
                    if(isValidJump(board, i, j, i+2, j+2)):
                        attacks += 1
                    if(isValidJump(board, i, j, i+2, j-2)):
                        attacks += 1

    score += attacks*0.5
    return score

while (not(redWin or blackWin)):
    if (turn == True): #Human turn
        checkers.displayBoard()
        print("Which piece would you like to move? Give an X coordinate and then a Y coordinate.")
        startX = int(input()) - 1
        startY = int(input()) - 1 #Take start coordinates

        if ((startX <= 7 and startX >= 0) and (startY <= 7 and startY >= 0) and type(checkers.board[startX][startY]) == Piece.Piece and checkers.board[startX][startY].colour == "red"): #A valid piece was chosen to move
            print("Where would you like to move the piece?")
            endX = int(input()) - 1
            endY = int(input()) - 1 #Take end coordinates

            if ((endX <= 7 and endX >= 0) and (endY <= 7 and endY >= 0)): #Valid coordinate
                if(isValidMove(checkers, startX, startY, endX, endY)):
                    checkers.board[endX][endY] = checkers.board[startX][startY] #Move piece to destination
                    checkers.board[startX][startY] = '#' #Empty start position
                    checkers.makeKings() #Make any kings that need to be made

                elif(isValidJump(checkers, startX, startY, endX, endY)):
                    #This section removes the enemy piece
                    while (True):
                        if(startX - endX > 0): #Upwards
                            if(startY - endY > 0): #Leftwards
                                checkers.board[startX-1][startY-1] = '#'
                            else: #Rightwards
                                checkers.board[startX-1][startY+1] = '#'
                        else:
                            if(startY - endY > 0): #Downwards
                                checkers.board[startX+1][startY-1] = '#'
                            else:
                                checkers.board[startX+1][startY+1] = '#'
                        
                        checkers.board[endX][endY] = checkers.board[startX][startY] #Move piece to destination
                        checkers.board[startX][startY] = '#' #Empty start position
                        checkers.makeKings() #Make any kings that need to be made
                        
                        #Now check for possible jumps in 2 (4 for kings) directions as jumps can be repeated in checkers if a piece jumps to a valid spot
                        moreJump = False
                        if (checkers.board[endX][endY].king):
                            if (endX-2 >= 0): #Make sure possible jumps would be in the board range
                                if (endY+2 <= 7):
                                    if(isValidJump(checkers, endX, endY, endX-2, endY+2)):
                                        moreJump = True
                                if (endY-2 >= 0):
                                    if(isValidJump(checkers, endX, endY, endX-2, endY-2)):
                                        moreJump = True
                            if (endX+2 <= 7):
                                if (endY+2 <= 7):
                                    if(isValidJump(checkers, endX, endY, endX+2, endY+2)):
                                        moreJump = True
                                if (endY-2 >= 0):
                                    if(isValidJump(checkers, endX, endY, endX+2, endY-2)):
                                        moreJump = True
                        else:
                            if (endX-2 >= 0): #Make sure possible jumps would be in the board range
                                if (endY+2 <= 7):
                                    if(isValidJump(checkers, endX, endY, endX-2, endY+2)):
                                        moreJump = True
                                if (endY-2 >= 0):
                                    if(isValidJump(checkers, endX, endY, endX-2, endY-2)):
                                        moreJump = True
                    
                        if(moreJump): #If there could be a new jump, give the user the option to jump again
                            checkers.displayBoard()
                            print("Would you like to jump again? (Y/N): ")
                            if (input() == 'N'):
                                break
                            else:
                                startX = endX
                                startY = endY
                                while (True):
                                    print("Where would you like to move the piece?")
                                    endX = int(input()) - 1
                                    endY = int(input()) - 1
                                    if (endX >= 0 and endX <= 7 and endY >= 0 and endY <= 7 and isValidJump(checkers, startX, startY, endX, endY)):
                                        break
                                    else:
                                        print("An error has occured. Did you choose a valid place to move to?")
                        else:
                            break     
                else:
                    print("An error occured. Did you choose a valid place to move to?")
                    continue
                turn = False #Flip the turn flag as it is now the AI's turn
            else:
                print("An error has occured. Did you choose a valid place to move to?")
        else:
            print("An error occured. Did you choose a valid piece to move?")
    else: #AI's Turn
        possibleMoves = []
        score = 0
        for row in range(8):
            for column in range(8):
                if (type(checkers.board[row][column]) == Piece.Piece and checkers.board[row][column].colour == "black"): #The AI will only attempt to move black pieces
                    if (checkers.board[row][column].king): #King checks all 4 directions
                        if (isValidMove(checkers, row, column, row+1, column+1)): #In the case that a move succeeds the board state has to be analyzed to see the outcome and assign it a score
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+1][column+1] = falseBoard.board[row][column]
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+1, column+1]) #Append the possible move and move on to the next possible move
                        if (isValidMove(checkers, row, column, row+1, column-1)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+1][column-1] = falseBoard.board[row][column]
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+1, column-1]) #Append the possible move and move on to the next possible move
                        if (isValidMove(checkers, row, column, row-1, column+1)): 
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row-1][column+1] = falseBoard.board[row][column]
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row-1, column+1]) #Append the possible move and move on to the next possible move
                        if (isValidMove(checkers, row, column, row-1, column-1)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row-1][column-1] = falseBoard.board[row][column]
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row-1, column-1]) #Append the possible move and move on to the next possible move
                        if (isValidJump(checkers, row, column, row-2, column-2)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row-1][column-1] = falseBoard.board[row][column]
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row-1, column-1]) #Append the possible move and move on to the next possible move
                        if (isValidJump(checkers, row, column, row-2, column-2)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row-2][column-2] = falseBoard.board[row][column]
                            falseBoard.board[row-1][column-1] = '#'
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row-2, column-2]) #Append the possible move and move on to the next possible move
                        if (isValidJump(checkers, row, column, row-2, column+2)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row-2][column+2] = falseBoard.board[row][column]
                            falseBoard.board[row-1][column+1] = '#'
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row-2, column+2]) #Append the possible move and move on to the next possible move
                        if (isValidJump(checkers, row, column, row+2, column-2)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+2][column-2] = falseBoard.board[row][column]
                            falseBoard.board[row+1][column-1] = '#'
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+2, column-2]) #Append the possible move and move on to the next possible move
                        if (isValidJump(checkers, row, column, row+2, column+2)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+2][column+2] = falseBoard.board[row][column]
                            falseBoard.board[row+1][column+1] = '#'
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+2, column+2]) #Append the possible move and move on to the next possible move

                    else:
                        if (isValidMove(checkers, row, column, row+1, column+1)): #In the case that a move succeeds the board state has to be analyzed to see the outcome and assign it a score
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+1][column+1] = falseBoard.board[row][column]
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+1, column+1]) #Append the possible move and move on to the next possible move
                        if (isValidMove(checkers, row, column, row+1, column-1)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+1][column-1] = falseBoard.board[row][column]
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+1, column-1]) #Append the possible move and move on to the next possible move
                        if (isValidJump(checkers, row, column, row+2, column-2)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+2][column-2] = falseBoard.board[row][column]
                            falseBoard.board[row+1][column-1] = '#'
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+2, column-2]) #Append the possible move and move on to the next possible move
                        if (isValidJump(checkers, row, column, row+2, column+2)):
                            falseBoard = generateFalseBoard()
                            falseBoard.board[row+2][column+2] = falseBoard.board[row][column]
                            falseBoard.board[row+1][column+1] = '#'
                            falseBoard.board[row][column] = '#'
                            falseBoard.makeKings()
                            score = judge(falseBoard) #Assign a score to the board state
                            possibleMoves.append([score, row, column, row+2, column+2]) #Append the possible move and move on to the next possible move

        #Now that all possible moves have been computed, find the highest scoring move
        max = -1000 #Far lower than any actual score, will make it easy to find real max
        for move in possibleMoves:
            if (move[0] > max):
                max = move[0] #Set the new max to find the best scores

        bestMoves = []
        for move in possibleMoves:
            if (move[0] == max):
                bestMoves.append(move)

        #bestMoves is now a list containing all moves with the highest score value, pick a random one of these
        move = random.choice(bestMoves)

        if isValidJump(checkers, move[1], move[2], move[3], move[4]):
            while (True):

                if(move[1] - move[3] > 0): #Upwards
                    if(move[2] - move[4] > 0): #Leftwards
                        checkers.board[move[1]-1][move[2]-1] = '#'
                    else: #Rightwards
                        checkers.board[move[1]-1][move[2]+1] = '#'
                else:
                    if(move[2] - move[4] > 0): #Downwards
                        checkers.board[move[1]+1][move[2]-1] = '#'
                    else:
                        checkers.board[move[1]+1][move[2]+1] = '#'

                checkers.board[move[3]][move[4]] = checkers.board[move[1]][move[2]]
                checkers.board[move[1]][move[2]] = '#'

                #The following code attempts to simulate the multi-jump feature of checkers, multijumps are almost always a good idea so the AI will take them
                if (checkers.board[move[3]][move[4]].king):
                    if (isValidJump(checkers, move[3], move[4], move[3]+2, move[4]+2)):
                        move[1] = move[3]
                        move[2] = move[4]
                        move[3] = move[3]+2
                        move[4] = move[4]+2
                        continue
                    elif (isValidJump(checkers, move[3], move[4], move[3]+2, move[4]-2)):
                        move[1] = move[3]
                        move[2] = move[4]
                        move[3] = move[3]+2
                        move[4] = move[4]-2
                        continue
                    elif (isValidJump(checkers, move[3], move[4], move[3]-2, move[4]+2)):
                        move[1] = move[3]
                        move[2] = move[4]
                        move[3] = move[3]-2
                        move[4] = move[4]+2
                        continue
                    elif (isValidJump(checkers, move[3], move[4], move[3]-2, move[4]-2)):
                        move[1] = move[3]
                        move[2] = move[4]
                        move[3] = move[3]-2
                        move[4] = move[4]-2
                        continue
                    break
                else:
                    if (isValidJump(checkers, move[3], move[4], move[3]+2, move[4]+2)):
                        move[1] = move[3]
                        move[2] = move[4]
                        move[3] = move[3]+2
                        move[4] = move[4]+2
                        continue
                    elif (isValidJump(checkers, move[3], move[4], move[3]+2, move[4]-2)):
                        move[1] = move[3]
                        move[2] = move[4]
                        move[3] = move[3]+2
                        move[4] = move[4]-2
                        continue
                    break

                      
        else: #Normal moves don't require special handling
            checkers.board[move[3]][move[4]] = checkers.board[move[1]][move[2]]
            checkers.board[move[1]][move[2]] = '#'

        checkers.makeKings()
        turn = True #Human's turn

  #Now check for win conditions
    redWin = True
    blackWin = True
    for line in checkers.board:
        for item in line:
            if (type(item) == Piece.Piece and item.colour == "black"):
                redWin = False
            elif (type(item) == Piece.Piece and item.colour == "red"):
                blackWin = False 

#Display win or loss message

if (redWin):
    print("You win!")
else:
    print("You lost :(")   
