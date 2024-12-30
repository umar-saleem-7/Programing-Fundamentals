from random import *
def main():
    i = 1
    max = 0
    c = 0
    while i <= 10:
        n1 = randint(1,100)
        n2 = randint(1,100)
        n3 = randint(1,100)
        print(f'set {i} :{n1} {n2} {n3}   \t',end='')
        avg = (n1 + n2 + n3)/3
        print('Average :',avg)
        if avg > max:
            max = avg
            c = i
        i = i + 1
    print(f'set {c} has highest average = {max}')
main()
