# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 4.19
# Date: 9/5/2024
from math import *

############ Part A ############

a = 1 / 7 
print(f'a = {a}') 
b = a * 7 
print(f'b = a * 7 = {b}')
#the value of b is returned as 1.0 
#this is because the varible a repersents a floating
#point number, ergo when used in arthmitic equations, it'll
#return a float

c = 2 * a 
d = 5 * a 
f = c + d 
print(f'f = 2 * a + 5 * a = {f}')

#The code returns .9 repeating. 5 * a and 2 * a can only repersent so much percision
# so when they get added together, they only add their finite points of percision,
# therefore being equivalant to .9 repeating

x = sqrt(1 / 3) 
print(f'x = {x}') 
y = x * x * 3 
print(f'y = x * x * 3 = {y}')
z = x * 3 * x 
print(f'z = x * 3 * x = {z}')

#the value was not 1

############ Part B ############

TOL = 1e-10
# check if b and f are equal within specified tolerance
if abs(b - f) < TOL: 
    print(f'b and f are equal within tolerance of {TOL}')
else: 
    print(f'b and f are NOT equal within tolerance of {TOL}')

if abs(y - z) < TOL: 
    print(f'y and z are equal within tolerance of {TOL}')
else: 
    print(f'y and z are NOT equal within tolerance of {TOL}')

############ Part C ############

m = 0.1 
print(f'm = {m}') 
n = 3 * m 
print(f'n = 3 * m = 0.3 {n==0.3}')
p = 7 * m
print(f'p = 7 * m = 0.7 {p==0.7}')
q = n + p
print(f'q = n + p = 1 {q==1}')