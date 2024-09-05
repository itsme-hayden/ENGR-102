# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 3.20
# Date: 9/2/2024

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here

num = float(input("Please enter the side length: "))
print("")
printresult("triangle", num, (sqrt(3) / 4) * pow(num,2))
printresult("square", num, num * num)
printresult("pentagon", num, 0.25 * sqrt(5 * (5 + 2 * sqrt(5))) * pow(num, 2))
printresult("hexagon", num, (3 * sqrt(3)) / 2 * pow(num, 2))
printresult("dodecagon", num, 3 * (2 + sqrt(3)) * pow(num,2))