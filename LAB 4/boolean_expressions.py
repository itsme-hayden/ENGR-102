# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   4.17 LAB
# Date:         9/10/24
from math import *
#i'm here
def torf(TorF):
    return (TorF == "True" or TorF == "t" or TorF =="T" or TorF == "true")

############ Part A ############
#we must take three inputs from the user (vars a, b, and c) and set them as 
#boolean varibles, however we cannot use if-else. this is tricky

a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

a = torf(a)
b = torf(b)
c = torf(c)


############ Part B ############

print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
xor = not a and b or a and not b
odd = (int(a) + int(b) + int(c)) == 1 or (int(a) + int(b) + int(c)) == 3
print(f"XOR: {xor}")
print(f"Odd number: {odd}")
############ Part D ############
# (optional) (we are doing it)

ex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
ex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

print("Complex 1:",ex1)
print("Complex 2:",ex2)
print("Simple 1:", ex1)
print("Simple 2:", ex2)



