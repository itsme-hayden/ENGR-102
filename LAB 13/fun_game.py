# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   13 Team LAB
# Date:         11/24/24
from random import shuffle

class Pawn:
    def __init__(self,color, id) -> None:
        '''Initializes the pawn object by assigning a color and number of spaces remaing until the end'''
        self.id = id
        self.color = color
        self.spaces = 65
        self.safe = False

    def spacesLeft(self):
        '''returns how many spaces the pawn has until reacing the goal'''
        return self.spaces
    
    def spacesMoved(self, n):
        '''Moves the pawn n number of spaces'''
        self.spaces -= n
        if self.spaces < 0:
            self.spaces = 0
    
    def setPosition(self, pos):
        '''Moves the pawn to given position so that the pawn has pos spaces remaining'''
        self.spaces = pos
    
    def returnColor(self):
        '''returns the color of the pawn, color cannot be changed once initalized'''
        return self.color
    
    def returnID(self):
        '''returns the ID of the pawn'''
        return self.id
    
    def atHome(self):
        '''updates the safe varible to True indicating pawn is in safe region'''
        self.safe = True

    def isSafe(self): 
        '''returns if the pawn can be sorried or not'''
        return self.safe
    
    def __str__(self) -> str:
        '''prints string information of color and spaces left'''
        return f"{self.returnColor()} pawn {self.returnID()} has {self.spacesLeft()} spaces remaining"
    
    ##ENDD OF CLASS##
    
def instructions():
    '''will print the instructions to the terminal'''
    print("The objective is to be the first player to get all three of their colored pawns from their start space, around the board to their 'home' space. The pawns are moved in a clockwise direction. Movement of pawns is directed by the drawing of a card.")
    print("The number on the card that the user draws is how many spaces forward the user will move")
    print("The user will be prompted to choose which pawn to move")

def isValidUserInput(txt:str):
    '''Checks if the user entered a d i or q'''
    if txt.strip() == "d" or txt.strip() == 'i' or txt.strip() == 'q':
        return True
    return False

def isGameOver(pawns:dict) -> bool:
    '''checks if a win condition as been met, if so returns True'''
    for i in pawns.values(): 
        tot = 0
        for j in i:
            tot += j.spacesLeft()
        if tot == 0:
            return True
    return False
        

def Sorry(pawnInitial: Pawn, pawnFinal: Pawn):
    '''runs for when the sorry card is activated, returns no value, swaps the position of two pawns'''
    temp = pawnInitial.spacesLeft()
    pawnInitial.setPosition(pawnFinal.spacesLeft())
    pawnFinal.setPosition(temp)
    


def createDeck() -> list:
    '''creates a new deck of cards and randomly shuffles them'''
    deck = [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, "Sorry"] * 4
    shuffle(deck)
    return deck

def drawCard(deck: list):
    '''returns the card on the top of the pile, if the deck is empty, function will create a new one'''
    try:
        card = deck.pop()
    except:
        deck = createDeck()
        card = deck.pop()
    return card

def whoWon(players:dict) -> str:
    '''checks which player met win condition'''
    for i in players: 
        tot = 0
        for j in players[i]:
            tot += j.spacesLeft()
        if tot == 0:
            return f"{i} player won the game!"
    return "NO ONE WON"



###MAIN CODE###    


deck = createDeck()

## assign pawns and initalize in array as values with players as keys
dick = {
    "Red": [Pawn('Red',1),Pawn('Red',2),Pawn('Red',3)],
    "Yellow": [Pawn('Yellow',1),Pawn('Yellow',2),Pawn('Yellow',3)],
    "Green": [Pawn('Green',1),Pawn('Green',2),Pawn('Green',3)],
    "Blue": [Pawn('Blue',1),Pawn('Blue',2),Pawn('Blue',3)]
}
##main game loop
quit = False
while not isGameOver(dick) and not quit:
    
    for i in dick:
    ## user goes first
        userinput = input(f"It is {i}'s turn \nEnter 'd' for draw or 'i' for instructions or 'q' to quit:")
        while not isValidUserInput(userinput):
            print('Invalid input!')
            userinput = input(f"It is {i}'s turn\nEnter 'd' for draw or 'i' for instructions or 'q' to quit:")
        while userinput == 'i':
            instructions()
            userinput = input(f"It is {i}'s turn\nEnter 'd' for draw or 'i' for instructions or 'q' to quit:")
        if userinput == 'q':
                quit = True
                break
        user_card = drawCard(deck)
        print(f"You drew a {user_card} card")
        
        if user_card == 'Sorry':
            for j in dick[i]:
                print(j)
            dickindexself = int(input('Which of your pawns would you like to move:')) -1
            while dickindexself > 2 or dickindexself< -1: 
                print('invalid pawn')
                dickindexself = int(input('Which of your pawns would you like to move:'))
            dickKeyOther = input(f'Which player would you like to swap with:')
            while dickKeyOther not in dick.keys() or dickKeyOther == i: 
                print('invalid player')
                dickKeyOther = input(f'Which player would you like to swap with:')
            dickIndexOther = int(input(f'Which pawn:')) -1
            while dickindexself > 2 or dickindexself< -1: 
                print('invalid pawn')
                dickIndexOther = int(input('Which pawn:'))
            Sorry(dick[i][dickindexself],dick[dickKeyOther][dickindexself])
            for j in dick[i]:
                print(j)
            for j in dick[dickKeyOther]:
                print(j)


        else:    
            for j in dick[i]:
                print(j)
            pawn_to_move = int(input("Which pawn would you like to move?"))
            while not pawn_to_move in [1,2,3]:
                print("invalid pawn number")
                pawn_to_move = int(input("Which pawn would you like to move?"))
            dick[i][pawn_to_move - 1].spacesMoved(user_card)
            for j in dick[i]:
                print(j)
        if isGameOver(dick):
            break

f = open("winner.txt",'w')
f.write(whoWon(dick))
f.close()
print("Game is finished, results are in winner.txt")



        
        