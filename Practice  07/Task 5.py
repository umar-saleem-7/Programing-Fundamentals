#from random import *
#x = randint(1,1000)
#print(f'Number: {x}')
#For random numbers only
x = int(input('Number: '))
a = x%2
b = x%3
c = x%5
d = x%7
if a == 0 and b == 0:
    print('Number is divisible by both 2 and 3')
elif b == 0 and c == 0:
    print('Number is divisible by both 3 and 5')
elif c == 0 and d == 0:
    print('Number is divisible by both 5 and 7')
elif a == 0 and c == 0:
    print('Number is divisible by both 2 and 5')
elif a == 0 and d == 0:
    print('Number is divisible by both 2 and 7')
elif b == 0 and d == 0:
    print('Number is divisible by both 3 and 7')
elif a == 0:
    print('Number is divisible by 2 only')
elif b == 0:
    print('Number is divisible by 3 only')
elif c == 0:
    print('Number is divisible by 5 only')
elif d == 0:
    print('Number is divisible by 7 only')
elif a == 0 and b == 0 and c == 0 and d == 0:
    print('Number is divisible by 2 , 3 , 5 , 7')
