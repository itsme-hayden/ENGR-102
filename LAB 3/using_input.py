# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 3.19
# Date: 9/1/2024
from math import*

#Renolyd's number
print("This program calculates the Reynolds number given velocity, length, and viscosity")
vel = float(input("Please enter the velocity (m/s): "))
len = float(input("\nPlease enter the length (m): "))
vis = float(input("\nPlease enter the viscosity (m^2/s): "))
Re = (vel * len) / vis
print(f"Reynolds number is {Re:.0f}") 

#wavelength
print("This program calculates the wavelength given distance and angle")
dis = float(input("Please enter the distance (nm): "))
ang = float(input("\nPlease enter the angle (degrees): "))
wavelength = 2 * dis * sin(radians(ang)) #in order to get sin() of 35 degrees, must transform to radians
print(f"Wavelength is {wavelength:.4f} nm")

#Arps equation
print("This program calculates the production rate given time, initial rate, and decline rate")
t = float(input("Please enter the time (days): "))
i = float(input("\nPlease enter the initial rate (barrels/day): "))
d = float(input("\nPlease enter the decline rate (1/day): "))
Arps = i / ((1 + 0.8 * d * t) ** (1 / 0.8))
print(f"Production rate is {Arps:.2f} barrels/day\n")

print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
initial_mass = float(input("Please enter the initial mass (kg): "))
final_mass = float(input("\nPlease enter the final mass (kg): "))
velocity = float(input("\nPlease enter the exhaust velocity (m/s): "))
rocket = velocity * log(initial_mass / final_mass)
print(f"Change of velocity is {rocket:.1f} m/s")





