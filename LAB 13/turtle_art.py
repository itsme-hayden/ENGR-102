# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Hayden Futch
# Section: 569
# Assignment: Lab 13
# Date: 11/24/2024
import turtle as t

def parta(degree):
    '''A function that connects a drawing given an angle and enough iterations'''
    t.dot(10, "red")
    while True:
        t.left(degree)
        t.forward(300)
        if abs(t.pos()) < 1: #check if at beginning
            break
    #t.done()

def partb(seq: str):
    '''makes a connected shape based of a sequence of 1s and 0s'''
    t.dot(10, "red")
    while True:
        for i in seq:
            if i == '0':
                t.left(30)
                t.forward(30)
            else:
                t.left(-114)
                t.forward(30)
        if abs(t.pos()) < 1: #check if at beginning 
            break
    #t.done()

def partc(seq:str,zero_angle:int,one_angle:int):
    '''uses a spiral sequence to make a spiral'''
    t.dot(10,'red')
    l = len(seq) // 100 #make the lines short enough to fit
    for i in seq:
        if i == '0':
            t.left(zero_angle)
            t.forward(l)
        else:
            t.left(one_angle)
            t.forward(l)


parta(160)
input()
t.reset()
parta(141)
input()
t.reset()
partb("01001")
input()
t.reset()
partb("01001011")
input()
t.reset()
seq1 = ""
for i in range(20):
    seq1 += '1'
    for j in range(i):
        seq1 += '0'
partc(seq1, 0, 90)
input()
t.reset()
partc(seq1,0,30)
input()
t.reset()
seq2 = ""
for i in range(50):
    seq2 += '1'
    for j in range(i):
        seq2 += '0'
partc(seq2, 0, 150)
input()
t.reset()
partc(seq2, 5, 108)
input()
t.done()
