from random import *
x1 = randint(1,10)
x2 = randint(1,10)
x3 = randint(1,10)
#print(x1,x2,x3)
if x1 + 2 == x2 or x1 +2 == x3:
    print('OK')
elif x2 + 2 == x1 or x2 + 2 == x3:
    print("OK")
elif x3 + 2 == x1 or x3 + 2 == x2:
    print('OK')
else:
    print('SORRY')