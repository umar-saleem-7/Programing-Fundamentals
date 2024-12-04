from random import *

a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
disc = b * b  - (4 * a * c)
x = 2 * a
if a == 0:
    print('equation is linear has only one root')
elif disc < 0:
    print('roots are imaginary')
else:
    root_1 = (-b - (disc) ** 0.5) / x
    root_2 = (-b + (disc) ** 0.5) / x
    print('Root 1 =',root_1)
    print('Root 2 =',root_2)