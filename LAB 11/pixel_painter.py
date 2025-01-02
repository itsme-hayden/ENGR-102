# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 11
# Date: 10/29/2024

#input

filename = input("Enter the filename: ")
char = input("Enter a character: ")

#file managment

f = open(filename, "r")
fout = open(filename[:-3] + "txt","w")

for i in f:
    line = i.split(",")
    c = 0
    for j in line:
        if c % 2 == 0:
            for k in range(int(j)):
                fout.write(" ")
        else:
            for k in range(int(j)):
                fout.write(char)
        c += 1
    fout.write("\n")

print(filename[:-3] + "txt created!")
f.close()
fout.close()