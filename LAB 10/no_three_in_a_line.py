# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hayden Futch
#               Patrick Murphy
#               Steven Sooudi
#               Serjio Maldonado
# Section:      569
# Assignment:   LAB 10 TEAM
# Date:         10/24/2024
from random import randint

def isLine(x1, y1, x2, y2, x3, y3):
    if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
        return True
    return False

def no_three_in_line(n):
    points = []
    
    # Strategy: Place points in a staggered fashion
    while len(points) < n:
        point = (randint(0, n - 1), randint(0, n - 1))
        flag = True # indicates wether the point should be added or not
        if len(points) > 2:
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    if isLine(point[0], point[1], points[i][0], points[i][1], points[j][0], points[j][1]):
                        flag = False
        if flag:
            points.append(point)

        
    
    return points

# Example usage:
#n = 4
#points = no_three_in_line(n)
#print(points)
