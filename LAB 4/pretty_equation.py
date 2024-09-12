# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   4.16 LAB
# Date:         9/3/24
from math import *

#TODO: we need to take in three intergers as coeffiecents to quadratic equation
# three if statments are needed:
# - if the number is negative
#       we need to change (+) to (-) in the equation in print statment (terenary statment??)
# - if the number is 1
#       we ommitt the coefficent in the print statment
# - if the number is 0
#       we omitt the coefficent and the varible and the (+ / -) sign
#       because of this condition, we may need to have the print statments inside of if statments
#       that checks wether or not the coeffiecent is non-zero
#
# example print statment: print(f"The quadratic equation is ")

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

if A == 1 :
    Var1 = "x^2"
elif A == 0 :
    Var1 = ""
elif A == -1:
    Var1 = "- x^2"
elif A < -1:
    Var1 =  f"- {abs(A)}x^2"
elif A > 1:
    Var1 = f"{A}x^2"
    

if A == 0:
    if B == 1 :
        Var2 = "x"
    elif B == 0 :
     Var2 = ""
    elif B > 1:
        Var2 = f"{B}x"
    elif B < 0:
        Var2 = f"- {abs(B)}x"
elif B == 1 :
    Var2 = "+ x"
elif B == 0 :
    Var2 = ""
elif B == -1:
    Var2 = f"- x"
elif B > 1:
    Var2 = f"+ {B}x"
elif B < 0:
    Var2 = f"- {abs(B)}x"

if B == 0:
    if C == 1 :
        Var3 = "x"
    elif C == 0 :
     Var3 = ""
    elif C > 1:
        Var3 = f"{C}"
    elif C < 0:
        Var3 = f"- {abs(C)}"   
elif C == 1 :
    Var3 = "+ 1"
elif C == 0 :
    Var3 = ""
elif C < 0:
    Var3 =  f"- {abs(C)}"
elif C > 1:
    Var3 = f"+ {C}"

if A != 0 and B != 0 and C != 0:
    print(f"The quadratic equation is",Var1, Var2, Var3, "= 0")
elif A != 0 and B == 0 and C != 0: 
    print(f"The quadratic equation is", Var1, Var3, "= 0")
elif A != 0 and B == 0 and C ==0:
    print(f"The quadratic equation is", Var1, "= 0")
elif A != 0 and B != 0 and C ==0:
    print(f"The quadratic equation is",Var1, Var2, "= 0")
elif A == 0 and B != 0 and C !=0:
    print(f"The quadratic equation is", Var2, Var3, "= 0")
