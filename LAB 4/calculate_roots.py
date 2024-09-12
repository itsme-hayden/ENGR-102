# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 4.21
# Date: 9/11/2024
from math import*

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
D = (B ** 2) - 4*A*C

#TODO fix all the random varibles and make more readable
if A == 0 and B != 0:
    root = (-1 * C) / B
    print(f"The root is x = {root}")
elif A == 0 and B == 0 and C != 0:
    print("You entered an invalid combination of coefficients!")
elif A == 0 and B == 0 and C == 0:
    print("ERROR: i didn't expect this to be a test case")
elif D < 0:
    rootR = (-1*B) / (2*A)
    rooti = (abs(D)) / (2*A) / 2
    print(f"The roots are x = {rootR} + {rooti}i and x = {rootR} - {rooti}i")
else:
    root1 = ((-1*B) + sqrt(pow(B,2) - 4*A*C)) / (2*A)
    root2 = ((-1*B) - sqrt(pow(B,2) - 4*A*C)) / (2*A)
    if root1 == root2: 
        print(f"The root is x = {root1}")
    else:
        print(f"The roots are x = {root1} and x = {root2}")

