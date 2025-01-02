# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 5.5
# Date: 9/18/2024
from math import*

num = float(input("Enter the excess temperature: ")) #this is the input from user

isValidNum = True #to print the right statement wether or not num is in range
ax = 1.3        #the x value of point A
ay = 1000       #the y value of point A
bx = 5          #the x value of point B
by = 7000       #the y value of point B
cx = 30         #the x value of point C
cy = 1.5*(10**6)#the y value of point C
dx = 120        #the x value of point D
dy = 2.5*(10**4)#the y value of point D
ex = 1200       #the x value of point E
ey = 1.5*(10**6)#the y value of point E

if(num < ax or num > ex):
    isValidNum = False
elif(num >= ax and num < bx):
    m = log10(by / ay)/log10(bx/ax)
    result = ay * ((num / ax) ** m)
elif(num >= bx and num < cx):
    m = log10(cy / by)/log10(cx/bx)
    result = by * ((num / bx) ** m)
elif(num >= cx and num < dx):
    m = log10(dy / cy)/log10(dx/cx)
    result = cy * ((num / cx) ** m)
elif(num >= dx and num < ex):
    m = log10(ey / dy)/log10(ex/dx)
    result = ey * ((num / ex) ** m)

if(isValidNum):
    print(f"The surface heat flux is approximately {result:.0f} W/m^2")
else:
    print("Surface heat flux is not available")