# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 4.20
# Date: 9/12/2024
from math import *

days = int(input("Please enter a positive value for day: "))
gadgets = 0
isvalidnum = True #this is a varible to run the correct print statement

if days >= 0 and days <= 10:
    gadgets = days * 10
elif days > 10 and days <= 50:
    gadgets += (days *(days + 1)) // 2 + 45
elif days > 50 and days < 101:
    gadgets = (days - 50) * 50 + 1320
elif days >= 101:
    gadgets = 3820
else:
    isvalidnum = False

if isvalidnum:
    print(f"The sum total number of gadgets produced on day {days} is {gadgets}")
else:
    print("You entered an invalid number!")