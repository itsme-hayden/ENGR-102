# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 469
# Assignment:   3.17 LAB
# Date:         8/27/24
from math import*

num = input("Please enter the quantity to be converted: ") #recieve input from user
num = float(num)
print(f"{num:.2f} pounds force is equivalent to {num * 4.44822:.2f} newtons") 
print(f"{num:.2f} meters is equivalent to {num * 3.28084:.2f} feet")
print(f"{num:.2f} atmospheres is equivalent to {num * 101.325:.2f} kilopascals")
print(f"{num:.2f} watts is equivalent to {num * 3.4121416:.2f} BTU per hour")
print(f"{num:.2f} liters per second is equivalent to {num * 15.850323074494:.2f} US gallons per minute")
print(f"{num:.2f} degrees Celsius is equivalent to {num * 9/5 + 32:.2f} degrees Fahrenheit")