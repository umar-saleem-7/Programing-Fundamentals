from random import *
def main():
    i = 1
    even = 0
    odd = 1
    while i <= 10:
        x = randint(1,100)
        if (x % 2) == 0:
            even = even + x
        else:
            odd = odd + x
        print('Random no. =',x)
        print('Sum of Even Numbers :',even)
        print('Sum of Odd Numbers :',odd)
        i = i + 1
main()
