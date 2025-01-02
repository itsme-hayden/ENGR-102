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

def isValidPassportFields(dick):
    if  int(dick['byr']) > 2008 or int(dick['byr']) < 1920:
        #print("ERROR BYR")
        return False
    if int(dick['eyr']) > 2034 or int(dick['eyr']) < 2024:
        #print('ERROR EYR')
        return False
    #print(dick["hgt"])
    if "cm" in dick["hgt"]:
        if int(dick['hgt'][:-2]) > 193 or int(dick['hgt'][:-2]) < 150:
           # print("ERROR HGT CM")
            return False
    elif "in" in dick['hgt']:
        if int(dick['hgt'][:-2]) > 76 or int(dick['hgt'][:-2]) < 59:
           # print ('ERROR HGT ')
            return False
    else:
        #print("ERROR HGT")
        return False
    

    for i in dick["hcl"]:
        if not i in ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9','#']:
           # print("ERROR HCL")
            return False
    
    if not len(dick['hcl']) == 7: # and not ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9','#'] in dick['hcl']:
        #print('ERROR HCL LEN')
        return False
    if dick['ecl'] != 'amb' and dick['ecl'] != 'blu' and dick['ecl'] != 'brn' and dick['ecl'] != 'gry' and dick['ecl']!= 'grn' and dick['ecl'] != 'hzl' and dick['ecl'] != 'oth':
        #print("ERROR ECL")
        return False
    if not len(dick["pid"]) ==  9:
        return False
    if dick['cid'][0] == "0":
        #print('ERROR CID')
        return False
    return True




def isValidPassport(txt:str) -> bool: #this method is to check if txt has all necessary passport criteria
    # byr 1920 - 2008
    # iyr still dont need
    # eyr 2024 - 2034
    # hgt 150 - 193 cm or 59 - 76
    # hcl  # followed by exactly 6 char (0-9) (a-f)
    # ecl one of "amb, blu, brn, gry, grn, hzl, oth"
    # cid three digit number not including leading zeros
    
    dick = {
        "byr": "1000",
        "iyr": "2010",
        "eyr": "2020",
        "hgt": "120 cm",
        "hcl": '0',
        "ecl": '0',
        "cid": "000",
        "pid":"999"
        }

    txt = txt.replace("\n"," ")
    txt = txt.strip()
    split_txt = txt.split(" ")
    for i in range(len(split_txt)):
        split_txt[i] = split_txt[i].split(":")
    #print(split_txt)
    for i in split_txt:
        #print(i)
        dick[i[0]] = i[1]
    return isValidPassportFields(dick)
    

######input######
file = input("Enter the name of the file: ") #here enter the name of the file
#file = r"LAB 11\scanned_passports-1.txt"
fo = open("valid_passports2.txt","w")
f = open(file,"r")

#so my assumption is that we're only changing the defined isvalidpassport function

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

  