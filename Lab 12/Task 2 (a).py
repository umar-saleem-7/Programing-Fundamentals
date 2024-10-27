from random import *
length=randint(5,9)
d=[[randint(1,9) for i in range (length)] for j in  range (length)]
for i in range (length):
    d[i][i]=0
x = randint(4,length-1)
for i in range (x):
    y = randint(0,length-1)
    z = randint(0,length-1)
    d[y][z]=-1
for i in range (length):
    d[i][i]=0
for i in range (length):
    for j in range (length):
        print(d[i][j],end=' ')
    print()
for i in range (length):
    print(f"City {i} has direct link with ",end='')
    for j in range (length):
        if d[i][j]!=-1 and i!=j:
            print(j,end=' ')
    print()