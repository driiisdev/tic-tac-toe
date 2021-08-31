"""
 | |   
-----
 | |   
-----
 | |   
"""
# guide for win check
"""
00|01|02   
---------
10|11|12  
---------
20|21|22  
"""  
# 3 x 3 board to accept input
board = [[" "," "," "],[" "," "," "],[" "," "," "]]

#function to create board
def createBoard():
    for row in range(5): #row = 0,1,2,3,4
        if row % 2 == 0: #0,2,4
            practicalRow = int(row / 2) # practicalRow = 0,1,2

            for column in range(5): #column = 0,1,2,3,4
                if column % 2 == 0: #0,2,4
                    practicalColumn = int(column / 2) #practicalColumn = 0,1,2
                    if column == 4:
                        print(board[practicalRow][practicalColumn])
                    else:
                        print(board[practicalRow][practicalColumn],end="")
                else:
                    print("|",end="")
        else:
            print("-" * 5)


#Horizontal win checks

def checkForWinhX():
    #Horizontal win for "X"
    if (board[0][0]=="X" and board[0][1]=="X"
    and board[0][2]=="X"):
        return True
    if (board[1][0]=="X" and board[1][1]=="X"
    and board[1][2]=="X"):
        return True
    if (board[2][0]=="X" and board[2][1]=="X"
    and board[2][2]=="X"):
        return True

def checkForWinhO():
    #Horizontal win for "O"
    if (board[0][0]=="O" and board[0][1]=="O"
    and board[0][2]=="O"):
        return True
    if (board[1][0]=="O" and board[1][1]=="O"
    and board[1][2]=="O"):
        return True
    if (board[2][0]=="O" and board[2][1]=="O"
    and board[2][2]=="O"):
        return True


#Vertical win checks

def checkForWinvX():
    #vertical win for "X"
    if (board[0][0]=="X" and board[1][0]=="X"
    and board[2][0]=="X"):
        return True
    if (board[0][1]=="X" and board[1][1]=="X"
    and board[2][1]=="X"):
        return True
    if (board[0][2]=="X" and board[1][2]=="X"
    and board[2][2]=="X"):
        return True

def checkForWinvO():
    #vertical win for "O"
    if (board[0][0]=="O" and board[1][0]=="O"
    and board[2][0]=="O"):
        return True
    if (board[0][1]=="O" and board[1][1]=="O"
    and board[2][1]=="O"):
        return True
    if (board[0][2]=="O" and board[1][2]=="O"
    and board[2][2]=="O"):
        return True


#Diagonal win checks

def checkDiagonalX():
    #Diagonal win for "X"
    if (board[0][0]=="X" and board[1][1]=="X"
    and board[2][2]=="X"):
        return True
    if (board[0][2]=="X" and board[1][1]=="X"
    and board[2][0]=="X"):
        return True
    
def checkDiagonalO():
    #Diagonal win for "O"
    if (board[0][0]=="O" and board[1][1]=="O"
    and board[2][2]=="O"):
        return True
    if (board[0][2]=="O" and board[1][1]=="O"
    and board[2][0]=="O"):
        return True

# win is set to false at default
win = False

# function to announce game over
def game_over():
    if win != True and move < 1 :
        print("game over")
        return

#player 1 goes first
player = 1

# the board is 3 x 3, it allows 9 moves
move = 9


while(move > 0 and win == False): # loop for move is less than and win is false

    print("players turn:", player) # print player's turn

    MoveRow = int(input("please enter row: ")) -1 #user enters (1-3), sub -1, enter: 0,1,2
    MoveColumn = int(input("please enter column: ")) -1 #user enters (1-3), sub -1, enter: 0,1,2

    if player == 1: #if player 1 goes first
        if board[MoveRow][MoveColumn] == " ":  #if the entered row n column on the board is empty
            board[MoveRow][MoveColumn] = "X" #if empty, enter X
            player = 2  # player 2 goes next
            move -= 1   #move is deducted by 1
        createBoard()

        #Here check for "X" win in all ways
        if checkForWinhX()==True: # if X wins horizontally
            print("Player one wins!")
            win = True
            break
        
        if checkForWinvX() == True: # if X wins vertically
            print("Player one wins!")
            win = True
            break

        if checkDiagonalX() == True: #if X wins diagonally
            print("Player one wins!")
            win = True
            break

    else:
        if board[MoveRow][MoveColumn] == " ": #if the entered row n column on the board is empty
            board[MoveRow][MoveColumn] = "O"  #if empty, enter O
            player = 1  #player 1 goes again
            move -= 1   #move is deducted by 1
        createBoard()

        #Here check for "O" win in all ways
        if checkForWinhO()==True: # if O wins horizontally
            print("Player two wins!")
            win = True
            break
        
        if checkForWinvO() == True: # if O wins vertically
            print("Player two wins!")
            win = True
            break

        if checkDiagonalO() == True: # if O wins diagonally
            print("Player two wins!")
            win = True
            break

if __name__ == '__main__':
    game_over()   
    
