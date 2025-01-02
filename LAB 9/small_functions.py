# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 9.20
# Date: 10/20/2024
from math import*

def parta(r_sphere: float,r_hole: float):
    #sph_volume = (4/3) * pi * pow(r_sphere,3)
    #cyl_volume = pi * pow(r_hole,2) * r_sphere
    volume = (4/3) * pi * (r_sphere ** 2 - r_hole ** 2)**(3/2)
    #(1/6) * pi * r_sphere * 2 * (3 * pow(r_hole,2) + pow(r_sphere * 2, 2)) # r_sphere * 2 = h
    return volume

def partb(n: int):
    n = abs(n)
    if n % 2 == 1:  #if a number is odd, even numbers can never add up to it
        return False    
    for i in range(2,n,2):#this means all other numbers are even, and all even numbers can add up to an even number
        temp = 0
        temp_list = []
        for j in range(i,n,2):
            temp += j
            temp_list.append(j)
            if temp > n:
                break
            elif temp == n:
                return temp_list
    return False

def partc(char: str, name: str, company: str, email: str):
     max_len = max(len(name),len(company),len(email)) + 6
     card = char * max_len + "\n"
     name_spaces = ((max_len - 2) - len(name)) / 2 # find how much spaces are needed
     company_spaces = ((max_len - 2) - len(company)) / 2
     email_spaces = ((max_len - 2) - len(email)) / 2
     #build string
     card += char + (" " * floor(name_spaces)) + name + (" " * ceil(name_spaces)) + char + "\n"
     card += char + (" " * floor(company_spaces)) + company + (" " * ceil(company_spaces)) + char + "\n"
     card += char + (" " * floor(email_spaces)) + email + (" " * ceil(email_spaces)) + char + "\n"
     card += char * max_len + "\n"
     return card

def partd(arr: list):
    arr.sort() #just in case
    if len(arr) % 2 == 0:
        median = (arr[(len(arr) // 2) - 1] + arr[(len(arr) // 2)]) / 2
    else:
        median = arr[len(arr) // 2]
    return arr[0], int(median), arr[-1] #since it is sorted, 0 is min and len - 1 is max
          
def parte(times: list, distances: list):
    velocity = []
    for i in range(len(times) - 1): #java type for loop
        time = times[i + 1] - times[i]
        dis = distances[i + 1] - distances[i]
        velocity.append(dis / time)
    return velocity

def partf(arr: list):
    for i in arr:
        for j in arr:
            if i + j == 2028: # i think this is what it wants me to do
                return i * j
    return False

def partg(x: float, tol: float): # might work
    term = 100
    n = 1
    total = 0
    while True:
        term = 2 / (2 * n - 1) * pow(x, 2 * n - 1)
        if(abs(term) < tol):
            break
        total += term
        n += 1
    return total


