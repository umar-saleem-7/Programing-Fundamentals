from random import *
x1 = randint(1,1000)
x2 = randint(1,1000)
x3 = randint(1,1000)
print(x1,'\t',x2,'\t',x3)
if x2<x1:
    temp=x1
    x1=x2
    x2=temp
if x3<x1:
    temp=x1
    x1=x3
    x3=temp
if x3<x2:
    temp=x2
    x2=x3
    x3=temp
print(x1,'\t',x2,'\t',x3)
