from random import *
def main():
    i = 1
    x = 0
    while i <= 10:
        c = 0
        n1 = randint(0,255)
        n2 = randint(0,255)
        print('Character 1 :',chr(n1))
        print('Character 2 :',chr(n2))
        if n1 & 1 == n2 & 1:
            c = c + 1
        if n1 & 2 == n2 & 2:
            c = c + 1
        if n1 & 4 == n2 & 4:
            c = c + 1
        if n1 & 8 == n2 & 8:
            c = c + 1
        if n1 & 16 == n2 & 16:
            c = c + 1
        if n1 & 32 == n2 & 32:
            c = c + 1
        if n1 & 64 == n2 & 64:
            c = c + 1
        if n1 & 128 == n2 & 128:
            c = c + 1
        print(f'Character 1 and Character 2 has {c} similar bits')
        i = i + 1
        x = c + x
    print(f'Total number of similar bits are {x}')
main()
