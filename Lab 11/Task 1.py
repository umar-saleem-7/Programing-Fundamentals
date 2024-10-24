from random import *
def main ():
    length = 10
    x = [0] * length
    for i in range (length):
        x[i] = randint(10,99)
        print(x[i],end=' ')
    print()
    y = list((x[i] for i in range(len(x))))
    for i in range (length-1):
        for j in range (length-1):
            if y[j]>y[j+1]:
                y[j],y[j+1] = y[j+1],y[j]
        for j in range (length):
            print(y[j],end=' ')
        print()
    for i in range (length):
        for j in range (length):
            if x[i] == y[j]:
                print(f'{x[i]} is at position {j}')
main()
