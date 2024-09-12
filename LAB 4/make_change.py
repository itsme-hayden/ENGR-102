# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   4.15 LAB
# Date:         9/10/24
from math import *

###
# for this one we need to find out how much total change a person 
# needs and then use an if-else chain going down from coins of 
# largest denomination to smallest for example
# if change > 25
#   quarters = change // 25
#   change %= 25
# so on so forth
###

payed = float(input("How much did you pay?"))
cost = float(input("How much did it cost?"))
change = round((payed - cost) * 100)
quarters = 0
dimes = 0
nickles = 0
pennies = 0


print(f"You received ${payed - cost:.2f} in change. That is... ")

if change >= 25:
    quarters = int(change // 25)
    change %= 25
if change >= 10:
    dimes = int(change // 10)
    change %= 10
if change >= 5:
    nickles = int(change // 5)
    change %= 5
if change >= 1:
    pennies = int(change)

if quarters == 1:
    print("1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

if dimes == 1:
    print("1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

if nickles == 1:
    print("1 nickel")
elif nickles > 1:
    print(f"{nickles} nickels")

if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")