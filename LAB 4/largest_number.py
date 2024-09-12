# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 4.18
# Date: 9/5/2024
from math import*

num1 = float(input("Enter number 1: "))
num2 = float(input("\nEnter number 2: "))
num3 = float(input("\nEnter number 3: "))

if num1 > num2 and num1 > num3:
    print(f"The largest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is {num2}")
elif num3 > num1 and num3 > num2:
    print(f"The largest number is {num3}")
else:
    print(f"The largest number is {max(num1,max(num2,num3))}") #this would technically be enough to pass the tests, but i decided to
    # in the spirit of the challange