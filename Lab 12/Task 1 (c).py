from random import *
length=randint(5,9)
d=[[randint(1,9) for i in range (length)] for j in  range (length)]
for i in range (length):
    d[i][i]=0
for i in range (length):
    for j in range (length):
        print(d[i][j],end=' ')
    print()
direct_distance=0
min = 99999
for i in range(length):
    for j in range (length):
        if i!=j:
            direct_distance = d[i][j]
            if min>direct_distance:
                min=direct_distance
                c1=i
                c2=j
print(f"city {c1} and city {c2} has shortest direct distance {min}")
