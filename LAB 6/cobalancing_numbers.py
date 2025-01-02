# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 6.20
# Date: 9/24/2024

def first_half(n): #returns the sum of 1 through n
    tol = 0
    for i in range(1,n+1):
        tol += i
    return tol


num = int(input("Enter a value for n: "))

total = first_half(num)

i = 0
r = 1
while i < total:
    i += num + r
    r += 1

if i == total:
    print(f"{num} is a co-balancing number with r={r - 1}")
else:
    print(f"{num} is not a co-balancing number")