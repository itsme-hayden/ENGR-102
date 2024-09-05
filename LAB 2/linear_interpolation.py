# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 469
# Assignment:   2.8 LAB
# Date:         8/27/24

import math
#(y2-y1/x2-x1)(x-x1)+y1 
#y2 = 23028 
#y1 = 2028 
#x2 = 55
#x1 = 10 
#x = 25
print("Part 1:")
ISSposition25 = ((23028-2028)/(55-10))*(25-10)+2028 
print("For t = 25 minutes, the position p =", ISSposition25, "kilometers")



print("Part 2:")
ISSposition300 = (((23028-2028)/(55-10))*(300-10)+2028)%(2*math.pi*6745) 
print("For t = 300 minutes, the position p =", ISSposition300, "kilometers")