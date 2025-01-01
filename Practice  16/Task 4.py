from random import *
r = int(input('Rows :'))
c = int(input('Columns :'))
i = 1
while i <= r:
    a = 1
    while a <= c:
        x = randint(1,9)
        print(x,end=' ')
        a = a + 1
    i = i + 1
    print()
