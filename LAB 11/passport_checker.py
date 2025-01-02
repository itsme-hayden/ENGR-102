# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   10 Team LAB
# Date:         10/29/24

def isValidPassport(txt:str) -> bool: #this method is to check if txt has all necessary passport criteria
    fields = ["byr","eyr","hgt","hcl","ecl","pid", "cid"]
    for i in fields:
        if not i in txt:
            return False
    return True

######input######
file = input("Enter the name of the file: ") #here enter the name of the file
#file = r"LAB 11\scanned_passports-1.txt"
fo = open("valid_passports.txt","w")
f = open(file,"r")

#####main for loop#######
count = 0
str = ""
for i in f:
    str += i
    if i == "\n":
        b = isValidPassport(str)
        if b: 
            count += 1
            fo.write(str)
        str = ""
b = isValidPassport(str)
if b:
    count += 1
    fo.write(str)
        
print(f"There are {count} valid passports")

  
####output########
#HALLOWEEN 🎃#
#spooky season 👻👻#
