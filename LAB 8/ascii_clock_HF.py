# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Hayden Futch
# Section:      ENGR 102 569
# Assignment:   8.17 LAB
# Date:         10/17/24

def time24(time,returnList):              
    global ascii_dict 
    ascii_dict = {#Steven filled in dict
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



if clocktype:
   time24(input_time,printList)
else:
    time12(input_time,printList)

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
