# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 08:01:49 2020

@author: cis-user
"""
# no.6
name='Simon Peter John'
a=name.split()
b='*'
for i in range(0,3):
    print(a[i][0],end='')
    print(b*(len(a[i])-1),end='')

# no.7
list1=['Company 1','Company 2','Company 3']
list2=[]
for i in range(0,3):
    list2.append(list1[i].replace(' ','_'))
print(list2)

# no.8
number1=['1','2','3','4','5','6']
number2=['$','$','$','$','$','$']
number3=[x+y for x,y in zip(number1,number2)]
print(number3)

# no.9
number4=['1$', '2$', '3$', '4$', '5$', '6$']
number5=[]
for i in range(0,6):
    number5.append(number4[i].replace('$',''))
print(number5)

# no.10
c=[1,2,3,4]
d=[5,6,7,8]
e=list(zip(c,d))
print(e)

# no1-(1)
s='I love you and you love him and who loves who'
s1=s.split()
print(s1)

#no1-(2)
print(set(s1))
keys=(set(s1))

#no1-(3)
values=[0 for i in keys]
dictionary={keys:values for keys, values in zip(keys,values)}
print(dictionary)

#no1-(4)
for i in s1:
    dictionary[i]+=1
print(dictionary)




