from random import *
def main():
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
        for j in range (length):
            if i!=j and d[i][j]==-1:
                for k in range (length):
                    if i!=k and j!=k and d[i][k]!=-1 and d[k][j]!=-1:
                        print(f"city {i} has indirect link with city {j} via city {k}")
                        break
main()
