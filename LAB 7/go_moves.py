# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   7 Team LAB
# Date:         10/5/24
from math import*

def printBoard(board): #a method to print the board in a readable way
    for i in board:
        for j in i:
            print(j, end="")
        print("")

def isValidMove(board, x, y): #a method to check wether a set of inputs is within range and a stone isn't on that spot
    if (x < 0 or x > 8) or (y < 0 or y > 8):
        return False
    if board[x][y] != ".":
        return False
    return True


def updateBoard(board, x, y, white): #updates board given x,y, and wether its white turn or not
    if white:
        board[x][y] = chr(9679)
    else:
        board[x][y] = chr(9675)

## These are varibles to have color text
begin = '\x1b[1m'
end = '\x1b[39m\x1b[22m'
red = '\x1b[31m'
blue = '\x1b[34m'
green = '\x1b[32m'
## 

board =  [["." for i in range(9)] for j in range(9)] #initilize board with . charcters using list comprehnsion
move_count = 0 #counts the number of moves to determine who's move it is and to ensure their won't be an infinite loop
white_move = True #varible to determine wether or not it is white's turn
while move_count < 81:
    printBoard(board) #print board on every iteration

    #check if it is white or black's turn
    if move_count % 2 == 0:
        print(begin + blue + "Black's" + end + " Turn")
        white_move = False
    else:
        print(begin + blue + "White's" + end + " Turn")
        white_move = True
    
    #Ask for input from user and check if the user wants to stop
    xy = input("Enter two integers (0-8 inclusive) to place your piece, or type stop: ")
    if xy.lower() == "stop":
        break
    if not xy[0].isnumeric():
        print(begin + red + "ERROR:" + end + " Invalid Input")
        print("Ensure you input either a cordinate x,y or stop")
        continue

    #Actually update board given input
    x = int(xy[0])
    y = int(xy[2])
    if isValidMove(board, x, y):
        updateBoard(board, x, y, white_move)
        move_count += 1 #update move count only if it is a valid move
    else:
        print(begin + red + "ERROR:" + end + " Invalid Move")
        print("Ensure that space is already taken, and that inputs are not out of range")
