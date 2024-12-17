from random import *
def umar():
    i = 1
    while i <= 10:
        x1 = randint(1,1000)
        x2 = randint(1,1000)
        x3 = randint(1,1000)
        print(f'\nN1 :{x1}   N2 :{x2}   N3 :{x3}')
        if x1 < x2 and x1 < x3 and x2 < x3:
            x1,x2,x3 = x1,x2,x3
        elif x1 < x2 and x1 < x3 and x3 < x2:
            x1,x2,x3 = x1,x3,x2
        elif x2 < x1 and x2 < x3 and x1 < x3:
            x1,x2,x3 = x2,x1,x3
        elif x2 < x1 and x2 < x3 and x3 < x1:
            x1,x2,x3 = x2,x3,x1
        elif x3 < x1 and x3 < x2 and x1 < x2:
            x1,x2,x3 = x3,x1,x2
        elif x3 < x1 and x3 < x2 and x2 < x1:
            x1,x2,x3 = x3,x2,x1
        print(f'Numbers in ascending order  : {x1},  {x2},  {x3}')
        i = i + 1
umar()
