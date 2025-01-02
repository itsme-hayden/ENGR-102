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
# Date:         9/24/24
from math import*

n = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
sides_eq = layers*((4 + (4 + (layers - 1) * 4)) / 2) # i found this formula
tops_eq = layers*((1 + (1 + (layers - 1) * 2)) / 2)

SurfaceArea = sides_eq * pow(n,2) + tops_eq * pow(n,2)

print(f"You need {SurfaceArea:.2f} m^2 of gold foil to cover the pyramid")
