# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 1.13
# Date: 8/21/2024
from math import*

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is 2")
guess = 2
ans = 0
for i in range(8): #range goes from 0-7 inclusive
    x = 1 / (10 ** i)
    f = (1 - cos(x)) / (x ** 2)
    print(f)
    ans = f // 1
print("")
if ans == guess:
    print("I was right!")
else:
    print("My guess was a little off")