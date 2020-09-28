# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:01:52 2020

@author: cis-user
"""
#第一題
score = ['小徐',5,9,6,8,7,10,6]
a=score[1:8]
print (score[0])
print (('最多進了:'),max(a),'球')
print (('最少進了:'),min(a),'球')
b=sorted(a)
print (('進球數最多的三回合各投入:'),b[3],b[4],b[5],'球')
print (('進球數最少的三回合各投入:'),b[0],b[1],b[2],'球')
print ('小徐進籃的平均球數:',sum(b)/len(b),'球')

#第二題
for a in range(1,10):
    for b in range(1,10):
        print('%dx%d=%2d' % (a, b, a*b), end=' ')
    print()

#第三題
import random
a=random.randint(1,1000)
b='I love you'
print(b,end='')
for i in range(a):
    print(' so',end='')
print(' much')
    
