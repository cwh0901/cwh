# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 08:22:27 2020

@author: cis-user
"""
# 1
# a=input('請輸入一個數，輸出小於這個數的質數:')
# for i in range(2,int(a)):
#     b=0
#     for j in range(1,i+1):
#         if i%j==0:
#             b+=1
#     if b==2:
#         print (i,end=' ')

# 2
x=input('輸入一串數字(用,號隔開)，請由小到大排序:')
list=[]
list1=[]
list.append(x)
while len(list) > 0:
    m = min(list)
    list.remove(m)
    list1.append(m)
print(list1)


