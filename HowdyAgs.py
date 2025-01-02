from math import*

#this is a comment
#it is for human convinence
#but if you can write elegant code
#you don't need comments

x = float(input("Enter a number: "))

if x < 0:
    print("Error: negative numbers are not defined for numbers less than 0")
else:
    ans = log(x)
    print(f"The natural log of {x} is {ans}")
