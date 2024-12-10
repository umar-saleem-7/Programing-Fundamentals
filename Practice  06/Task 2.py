from random import *
x = randint(1,5)
y = randint(1,5)
print(f'Firsty Number:{x}')
print(f'Second Number:{y}')
diff = abs(x-y)
if x==y:
    print('Numbers are exactly equal')
elif diff<=1:
    print('Number are almost equal')
else:
    print('Number are not equal')