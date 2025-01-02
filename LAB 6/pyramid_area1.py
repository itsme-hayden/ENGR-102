# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
#                Serjio Maldonado

# Section:      ENGR 102 569
# Assignment:   6.13 LAB
# Date:         9/26/24

from math import*
m = float(input("Enter the side length in meters: "))
h = int(input("Enter the number of layers: "))               #I love coding
h += 1
SurfaceArea = 0
var = 0

for i in range(1,h):
    SurfaceArea += ((m*i)**2) +(m*i*m)*4
    var += (m*i)**2

SurfaceArea += (m*i)**2
SurfaceArea -= var

print(f"You need {SurfaceArea:.2f} m^2 of gold foil to cover the pyramid")