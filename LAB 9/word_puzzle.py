# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hayden Futch
#               Patrick Murphy
#               Steven Sooudi
#               Serjio Maldonado
# Section:      569
# Assignment:   9.19
# Date:         10/20/2024

def get_valid_letters(txt:str) -> str:                     #takes in one string and returns a string 
    newtxt = ''
    for i in range(0,len(txt)):
        if txt[i] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] and txt[i] not in newtxt: 
            newtxt += txt[i] #adds correct letter to newtxt
    return(newtxt) 

def is_valid_guess(letters:str,guess:str) -> bool:         #valid letters is the result from get_valid_letters
    #return a boolean; True only if guess contains exactly 10 letters from letters string
    if len(guess) != 10:                                   #checks if the guess is exactly 10 letters
        return False
    sorted_letters = "".join(sorted(letters))
    sorted_guess = "".join(sorted(guess))
    if sorted_letters == sorted_guess:
        return True
    return False

def check_user_guess(dividend:int, quotient:int, divisor:int, remainder:int) -> bool:
    if dividend == quotient * divisor + remainder:
        return True
    return False

def make_number(word:str,guess:str) -> int: #read doc to understand this
    #word = RUE, guess = TAKEOURSIM, result is 653
    #new_num = ''#letterdict = {[0]:'0',[1]:'1',[2]:'2',[3]:'3',[4]:'4',[5]:'5',[6]:'6', [7]:'7', [8]:'8', [9]:'9'}
    f_word = word.strip()
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    num = ""
    for i in f_word:
        index_digit = guess.index(i)
        num += nums[index_digit]

 
    return int(num)

   
   
def make_numbers(puzzle:str,guess:str) -> tuple: # a tuple of 4 ints
    #calls make number four times to create make_number
    puzzle1 = puzzle.split(',')
    puzzle2 = puzzle1[1].split("|")
    puzzle_tuple = (make_number(puzzle2[1],guess), make_number(puzzle1[0],guess), make_number(puzzle2[0],guess), make_number(puzzle1[-1],guess))

    return puzzle_tuple

    
def print_puzzle(puzzle: str):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = input("Enter a word arithmetic puzzle: ")
    #puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA" #TODONE: Make input
    print()
    print_puzzle(puzzle)
    print()
    valid_letters = get_valid_letters(puzzle)
    user_guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    if not is_valid_guess(valid_letters,user_guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    if is_valid_guess(valid_letters,user_guess):
        nums = make_numbers(puzzle, user_guess)
        if not check_user_guess(nums[0],nums[1],nums[2],nums[3]):
            print("Try again!")
        else:
            print("Good job!")
        
        
        
    
    

if __name__ == '__main__':
    main()




    