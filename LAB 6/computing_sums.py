# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 6.17
# Date: 9/21/2024
from math import *

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

sum = 0

for i in range(num1,num2+1): #have to add 1 to ensure you get num2
    sum += i    #just add i!
print(f"The sum of all integers from {num1} to {num2} is {sum}")