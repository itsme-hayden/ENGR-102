# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 2.11
# Date: 8/23/2024

# avalible lines
# x = 1
# y = 10
# z = 0
# x = y
# x += 1
# y += x
# y *= x
# z += x
# z += y
# print(z)

z = 0
x = 1
z += x
print(z)

z = 0
x += 1
y = 10
y *= x
z += y
x += 1
x += 1
z += x
z += x
print(z)

y = 10
x = y
y *= x
x = 1
z = 0
z += x
z += x
z += y
print(z)

z = 0
y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
y *= x
z += y
print(z)

z = 0
y = 10
x = 1
x = y
y *= x
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y
y = 10
x = 1
x = y
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y
y = 10
x = y
y += x
y += x
y += x
y += x
y += x
y += x
z += y
x = 1
x += 1
x += 1
x += 1
x += 1
z += x
print(z)