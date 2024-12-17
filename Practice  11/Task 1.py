from random import *
def umar():
    i = 1
    while i <= 10:
        x = randint(1,1000)
        y = randint(1,1000)
        print(f'first number : {x}   second number :{y}')
        if x>y:
            print('First random number is larger')
        else:
            print('Second random number is larger')
        i = i + 1
umar()
