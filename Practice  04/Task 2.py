from random import *
a = randint(1,10)
x = int(input('First chance : '))
y = int(input('Wrong, Second chance : '))
z = int(input('Again wrong, Third chance : '))
if a == x or a == y or a == z:
	print('WINNER')
	print(f'Number is {a}')
else:
	print('YOU LOSE')
	print(f'Number is {a}')
