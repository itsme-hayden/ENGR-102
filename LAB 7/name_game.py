# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 7.19
# Date: 9/26/2024
from math import*

def findIndexOfFirstVowel(str):
    vowel_indexes = []
    vowel_indexes.append(name.find("a"))
    vowel_indexes.append(name.find("e"))
    vowel_indexes.append(name.find("i"))
    vowel_indexes.append(name.find("o"))
    vowel_indexes.append(name.find("u"))
    vowel_indexes.append(name.find("y"))
    return min(i for i in vowel_indexes if i >= 0)

name = input("What is your name? ")
rhyme_name = ""
if name[0] == "A" or name[0] == "E" or name[0] == "I" or name[0] == "O" or name[0] =="U" or name[0] == "Y": #there has to be a better way using lists
    rhyme_name = name.lower()
else:
    rhyme_name = name[findIndexOfFirstVowel(name):]

print(f"{name}, {name}, Bo-B{rhyme_name}") #I don't know if this is
print(f"Banana-Fana Fo-F{rhyme_name}")     #better or worse than
print(f"Me Mi Mo-M{rhyme_name}")           #Java.substring()
print(f"{name}!")