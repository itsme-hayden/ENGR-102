# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   6.15 LAB
# Date:         9/24/24
from math import*

x = float(input("Enter a value for x: "))
while not (x > 0 and x <=2):
    x = float(input("Out of range! Try again: "))

tol = float(input("Enter the tolerance: "))

approx = 0
i = 1
while True: #runs forever
    n = ((x - 1) ** i) / i
    i += 1
    if(abs(n) < tol):
        break
    if i % 2 == 0:
        approx += n
    else:
        approx -= n

print(f"ln({x}) is approximately {float(approx)}") #float() forces 0.0
print(f"ln({x}) is exactly {log(x)}")
print(f"The difference is {abs(log(x) - approx)}")

