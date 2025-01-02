# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 7.20
# Date: 9/26/2024
from math import*

def balancedIndex(arr):
    for i in range(len(arr)):
        #print(f"i = {i}")
        left_total = 0
        right_total = 0
        #left
        for j in range(0,i + 1):
            left_total += int(arr[j])
            #print(i, end=" ")
        #right
        for j in range(i + 1,len(arr)):
            right_total += int(arr[j])
            #print(i, end=" ")
        if right_total == left_total:
            return i
    return -1

def sumOfHalf(arr, piv):
    total = 0
    for i in arr[:piv + 1]:
        total += int(i)
    return total


user_input = input("Enter numbers: ")

#place input into an int array
arr = user_input.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

pivot = balancedIndex(arr)

if pivot == -1:
    print("Cannot split evenly")
else:
    print(f"Left: {arr[0:pivot + 1]}")
    print(f"Right: {arr[pivot + 1:]}")
    print(f"Both sum to {sumOfHalf(arr,pivot)}")
