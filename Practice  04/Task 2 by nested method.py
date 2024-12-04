from random import *
a = randint(1,10)
x = int(input('Guess Number :'))
if a == x:
    print('WINNER')
else:
    y = int(input('Guess Number :'))
    if a == y:
        print('WINNER')
    else:
        z = int(input('Guess Number :3'))
        if a == z:
            print('WINNER')
        else:
            print('YOU LOSE')
            print(f'Number is {a}')