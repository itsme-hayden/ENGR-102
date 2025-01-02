# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 11
# Date: 10/29/2024

inf = open('game.txt','r')
out = open('coins.txt','w')

arr = []

for i in inf: # add the lines of the file to an array that is easier to work with
    arr.append(i.split())

inf.close() #no longer need the file

for i in arr: #make the numbers useable ints
    i[1] = int(i[1])

coin_total = 0
i = 0
while i < len(arr):
    if arr[i][0] == "coin":
        coin_total += arr[i][1]
        out.write(str(arr[i][1]) + "\n") 
        i += 1
    elif arr[i][0] == "jump":
        i += arr[i][1]
    elif arr[i][0] == "none":
        i += 1
        continue
    else:
        print("ERROR: arr[i][0] Value not reconized")
out.close()
print(f"Total coins collected: {coin_total}")
    
