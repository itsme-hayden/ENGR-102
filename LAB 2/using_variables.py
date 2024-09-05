# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 2.9
# Date: 8/22/2024
from math import*

Re_num = (9 * 0.875) / 0.0015 
xray_wavelength = 2 * 0.028 * sin(radians(35)) #in order to get sin() of 35 degrees, must transform to radians
Arps_oil_production = 100 / ((1 + 0.8 * 2 * 10) ** (1 / 0.8))
rocket_velocity = 2028 * log(11000 / 8300)


print("Reynolds number is", Re_num, "\nWavelength is", xray_wavelength,"nm\nProduction rate is", Arps_oil_production,"barrels/day\nChange of velocity is", rocket_velocity,"m/s")
