from random import *
x1 = randint(1,1000)
x2 = randint(1,1000)
x3 = randint(1,1000)
print(f'Numbers: {x1}   {x2}   {x3}')
if x3 > x2 and x2 > x1:
    print('Numbers are in order')
else:
    print('Numbers are not in order')