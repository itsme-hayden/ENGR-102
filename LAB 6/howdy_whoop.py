# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 6.16
# Date: 9/21/2024
from math import *

num1 = int(input("Enter an integer: "))
num2 = int(input("\nEnter another integer: "))

for i in range(1,101): 
    if i % num1 == 0: #I used if statements instead of elif statments because I would have to check for more
        print("Howdy") #conditions using elif
    if i % num2 == 0:
        print("Whoop")
    if i % num1 != 0 and i % num2 != 0:
        print(i)