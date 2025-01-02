# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   12 Team LAB
# Date:         11/12/24
import numpy as np

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4,2)
C = np.arange(6).reshape(2,3)
D = np.dot(A, B @ C)
Dt = np.transpose(D)
E = np.sqrt(D) / 2

print(f"A = {A}\n")
print(f"B = {B}\n")
print(f"C = {C}\n")
print(f"D = {D}\n")
print(f"D^T = {Dt}\n")
print(f"E = {E}\n")

