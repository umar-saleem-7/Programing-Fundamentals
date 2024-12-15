from random import *
a = randint(1,13)
b = randint(1,13)
c = randrange(0,4)
d = randrange(0,4)
x = randint(0,1)
y = randint(0,1)

if a == 1:
    q = 'Ace'
elif a == 11:
    q = 'Jack'
elif a == 12:
    q = 'Queen'
elif a == 13:
    q = 'King'
else:
    q = str(a)

if b == 1:
    w = 'Ace'
elif b == 11:
    w = 'Jack'
elif b == 12:
    w = 'Queen'
elif b == 13:
    w = 'King'
else:
    w = str(a)


if c == 0:
    e = 'Diamond'
elif c == 1:
    e = 'Heart'
elif c == 2:
    e = 'Spade'
else:
    e = 'Club'



if d == 0:
    r = 'Diamond'
elif d == 1:
    r = 'Heart'
elif d == 2:
    r = 'Spade'
else:
    r = 'Club'



if x == 0:
    t = 'Red'
else:
    t = 'Black'



if y == 0:
    u = 'Red'
else:
    u = 'Black'



if q == w:
    print('Both cards have same number')
else:
    print('Both cards have different number')


if e == r:
    print('Both cards have same type')
else:
    print('Both cards have different type')


if t == u:
    print('Both cards have same color')
else:
    print('Both cards have different color')

if (a - b == 1) or (b - a == 1):
    print('Cards are in sequence')



print(f'Number1 = {q}     Number2 = {w}   Type1 = {e}   Type2 = {r}   color1 = {t}   color2 = {u}')
