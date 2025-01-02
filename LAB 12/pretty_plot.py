# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 12
# Date: 11/5/2024
import numpy as np
import matplotlib.pyplot as plt

vector = np.array([[1], [2]])
matrix = np.array([[1.02,0.095],[-0.095,1.02]])
array = [[],[]]
array[0].append(vector[0][0])
array[1].append(vector[1][0])
for i in range(250):
    vector = np.dot(matrix,vector)
    array[0].append(vector[0][0])
    array[1].append(vector[1][0])

plt.plot(array[0],array[1])
plt.xlabel("x points of vector")
plt.ylabel("y points of vector")
plt.title("The golden ratio produced from continous dot products of a matrix and vector")
print(vector)
plt.show()