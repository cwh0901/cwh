# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("解一元二次方程式:ax**2+bx+c=0")
a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
y=(b**2) - (4*a*c)
x1 = (-b-y**0.5)/(2*a)
x2 = (-b+y**0.5)/(2*a)
print('解1:\n',x1)
print('解2:\n',x2)
