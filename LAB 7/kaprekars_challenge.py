# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 7.22
# Date: 9/28/2024
from math import*

def makeStrFourDigit(number:str): #Method to add leading zeros to a string that has a len < 4
    while len(number) < 4:
        number = "0" + number
    return number

def kOpperation(n): #Method that takes a num, creates two lists that have the digits sorted and reverse sorted
    aList = list(n) #then substracts the sorted list by the reverse list, then returns the diffrence
    dList = list(n)
    aList.sort(reverse=True)
    dList.sort(reverse=False)
    for i in range(4):
        aList[i] = int(aList[i])
        dList[i] = int(dList[i])
    aNum = 0
    dNum = 0
    for i in range(4):
        aNum += aList[i] * 10 ** (3 - i)
        dNum += dList[i] * 10 ** (3 - i)
    num = aNum - dNum
    num = str(num)

    if len(num) < 4:
        num = makeStrFourDigit(num)

    return num

    

def kapCount(n,c): #A RECURSIVE function that checks for the base case n = "6174" and returns an int c
    if n == "6174" or c > 8:
        #print(n)
        c += 1
        return c
    else:
        #print(int(n), end=" > ")
        c += 1
        return kapCount(kOpperation(n),c)

#main code#
count = 0
for i in range(10000):
    num = str(i)
    if len(num) < 4:
        num = makeStrFourDigit(num)
    if num[0] == num[1] and num[1] == num[2] and num[2] == num[3]:
        count += 1
    else:
        count += kapCount(num,0) - 1
print(f"Kaprekar's routine takes {count - 1} total iterations for all four-digit numbers")