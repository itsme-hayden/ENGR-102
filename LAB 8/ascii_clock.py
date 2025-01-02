# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
#                Serjio Maldonado
# Section:      ENGR 102 569
# Assignment:   8.17 LAB
# Date:         10/17/24

#inputs here 

#    #dictionary for digits and letters (numbers in this case) for time

def time24(time,returnList):              #Steven did this
    global ascii_dict 
    ascii_dict = {
"0":   [['0','0','0'],
        ['0',' ','0'],
        ['0',' ','0'],
        ['0',' ','0'],
        ['0','0','0']],
"1":   [[' ','1',' '],
        ['1','1',' '],
        [' ','1',' '],
        [' ','1',' '],
        ['1','1','1']],
"2":   [['2','2','2'],
        [' ',' ','2'],
        ['2','2','2'],
        ['2',' ',' '],
        ['2','2','2']],
"3":   [['3','3','3'],
        [' ',' ','3'],
        ['3','3','3'],
        [' ',' ','3'],
        ['3','3','3']],
"4":   [['4',' ','4'],
        ['4',' ','4'],
        ['4','4','4'],
        [' ',' ','4'],
        [' ',' ','4']],
"5":   [['5','5','5'],
        ['5',' ',' '],
        ['5','5','5'],
        [' ',' ','5'],
        ['5','5','5']],
"6":   [['6','6','6'],
        ['6',' ',' '],
        ['6','6','6'],
        ['6',' ','6'],
        ['6','6','6']],
"7":   [['7','7','7'],
        [' ',' ','7'],
        [' ',' ','7'],
        [' ',' ','7'],               
        [' ',' ','7']],
"8":   [['8','8','8'],
        ['8',' ','8'],
        ['8','8','8'],
        ['8',' ','8'],
        ['8','8','8']],
"9":   [['9','9','9'],
        ['9',' ','9'],
        ['9','9','9'],
        [' ',' ','9'],
        ['9','9','9']],
"A":   [[' ','A',' '],
        ['A',' ','A'],
        ['A','A','A'],
        ['A',' ','A'],
        ['A',' ','A']],
"M":   [['M',' ',' ',' ','M'],
        ['M','M',' ','M','M'],
        ['M',' ','M',' ','M'],
        ['M',' ',' ',' ','M'],
        ['M',' ',' ',' ','M']],
"P":   [['P','P','P'],
        ['P',' ','P'],
        ['P','P','P'],
        ['P',' ',' '],
        ['P',' ',' ']],
":": [[' '],
      [':'],
      [' '],
      [':'],
      [' ']],
" ": [[' '],
      [' '],
      [' '],
      [' '],
      [' ']]
    }                             
    for i in time:
        if i == ":":
            returnList.append(ascii_dict[':'])
        else:
            returnList.append(ascii_dict[i])
        returnList.append(ascii_dict[" "])   #space after each character
    returnList.pop()

def time12(time,returnList): #remove leading zeros by having an if statement that checks if time[0] == "0", if it is, replace the string with time[1:]
    if len(time) == 5:
        isAM = int(time[0:2]) < 12
    elif time[0] == "0":
        time = "12" + time[1:]
        isAM = True
    else:
        isAM = True
    if not isAM and int(time[0:2]) != 12:
        hour = str(int(time[0:2]) - 12)       #convert to 12 hour format
        time = hour + time[2:]               
    time24(time, returnList)                    
    if isAM:
        returnList.append(ascii_dict[' '])
        returnList.append(ascii_dict['A'])    #'A' for AM
        returnList.append(ascii_dict[' '])
        returnList.append(ascii_dict['M'])    #'M' for AM
    else:
        returnList.append(ascii_dict[' '])
        returnList.append(ascii_dict['P'])    #'P' for PM
        returnList.append(ascii_dict[' '])
        returnList.append(ascii_dict['M'])    #'M' for PM


printList = [] #a 2d array                                       #Patrick inputs
input_time = input("Enter the time: ")
clocktype = input("Choose the clock type (12 or 24): ")          #code picking military time or 12 hour clock (the clocktype)
prefchar = input("Enter your preferred character: ")   

while clocktype != "12" or clocktype != "24":
    if clocktype == "12" or clocktype == "24":
        break
    clocktype = input("Choose the clock type (12 or 24): ") 

clocktype = clocktype == "24"  #sets clocktype to boolean  

#the allowed prefered characters, and BTW I love coding
allowedchar = ["a","b","c","d","e","g","h","k","m","n","o","p","q","r","s","u","v","w","x","y","z","@","$","&","*","=", ""]

    
if prefchar not in allowedchar:
    while prefchar not in allowedchar:
        prefchar = input("Character not permitted! Try again: ") 

numdetect = 0

if clocktype:
   time24(input_time,printList)
else:
    time12(input_time,printList)

finalprint_list = []


# HAYDEN AND STEVEN, also patrick and surjio
for i in range(5):
    temp_List = []
    temp_String = ""
    for j in printList:
        finalprint = "".join(j[i])
        temp_List.append(finalprint)
    temp_String = "".join(temp_List)
    finalprint_list.append(temp_String)


if prefchar != "":
    for i in range(5):
        for j in range(0,10):
            finalprint_list[i] = str(finalprint_list[i]).replace(str(j),prefchar)

print()

for i in finalprint_list:
    print(f"{i}")

    


#if prefchar != "":
    #for i in range():
#we can move this later I'm just typing out of the way for now 

#for j in printList:
 #       print("".join(j[i]),end="")
  #  print()
#"".replac11e()