# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 6.19
# Date: 9/24/2024
import math

num = int(input("Enter a positive integer: "))
copy_of_num = num #quick and easy fix for n = 1 edge case, rather than put another if statment
count = 0 #count num of iterations

numlist = [] #i was being fancy
while num != 1:
    numlist.append(num)
    if num % 2 == 0:
        num = math.floor(math.sqrt(num))
    else:
        num = math.floor(math.pow(num, 3/2))
    count += 1

print(f"The Juggler sequence starting at {copy_of_num} is: ")
for i in numlist:
    print(f"{i}", end=", ")
print("1")
print(f"It took {count} iterations to reach 1")