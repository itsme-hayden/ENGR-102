# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   4.17 LAB
# Date:         9/3/24
from math import *

def torf(TorF):
    return (bool(TorF == "True" or TorF == "t" or TorF =="T"))

############ Part A ############
#we must take three inputs from the user (vars a, b, and c) and set them as 
#boolean varibles, however we cannot use if-else. this is tricky

a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

a = torf(a)
b = torf(b)
c = torf(c)

print(f"{a} {b} {c}")

############ Part B ############

print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
############ Part D ############
# (optional) (we are doing it)