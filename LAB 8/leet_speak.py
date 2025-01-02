# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 8.18
# Date: 10/10/2024
from math import*

#["a", "e", "o", "s", "t"]
leet_equivalant = {
    "a": "4",
    "e": "3",
    "o": "0",
    "s": "5",
    "t": "7"
}

txt = input("Enter some text: ")
print_txt = ""

for i in txt:
    if i in leet_equivalant.keys(): #checks if charcter i is in a list that repersents all key values
        print_txt += leet_equivalant[i]
    else:
        print_txt += i

print(f"In leet speak, \"{txt}\" is:\n{print_txt}")