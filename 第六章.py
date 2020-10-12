# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:22:21 2020

@author: cis-user
"""

# no.3
l1=[1,2,3,4,5]
l2=[6,5,4,3,2]
l3=[]
for i in range(0,5):
    if l1[i]>l2[i]:l3.append(l1[i])
    else:l3.append(l2[i])
print(l3)

# no.4
list1 = [1,2,3,4,5]
list2 = [6,5,4,3,2]
list3 = [False,False,True,False,True]
list4=[]
for i in range(0,5):
    if list3[i]==True:list4.append(list1[i])
    else:list4.append(list2[i])
print(list4)