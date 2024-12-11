from random import *
x1 = randint(1,1000)
x2 = randint(1,1000)
x3 = randint(1,1000)
x4 = randint(1,1000)
print(f'Numbers before condition: {x1}\t{x2}\t{x3}\t{x4}')

if x1<x2 and x1<x3 and x1<x4 and x2<x3 and x2<x4 and x3<x4:
	print(f'Numbers after condition: {x1}\t{x2}\t{x3}\t{x4}')
elif x1<x2 and x1<x3 and x1<x4 and x2<x3 and x2<x4 and x4<x3:
	print(f'Numbers after condition: {x1}\t{x2}\t{x4}\t{x3}')
elif x1<x2 and x1<x3 and x1<x4 and x3<x2 and x3<x4 and x2<x4:
	print(f'Numbers after condition: {x1}\t{x3}\t{x2}\t{x4}')
elif x1<x2 and x1<x3 and x1<x4 and x3<x2 and x3<x4 and x4<x2:
	print(f'Numbers after condition: {x1}\t{x3}\t{x4}\t{x2}')
elif x1<x2 and x1<x3 and x1<x4 and x4<x2 and x4<x3 and x2<x3:
	print(f'Numbers after condition: {x1}\t{x4}\t{x2}\t{x3}')
elif x1<x2 and x1<x3 and x1<x4 and x4<x2 and x4<x3 and x3<x2:
	print(f'Numbers after condition: {x1}\t{x4}\t{x3}\t{x2}')
elif x2<x1 and x2<x3 and x2<x4 and x3<x4 and x3<x1 and x1<x4:
	print(f'Numbers after condition: {x2}\t{x3}\t{x1}\t{x4}')
elif x2<x1 and x2<x3 and x2<x4 and x3<x4 and x3<x1 and x4<x1:
	print(f'Numbers after condition: {x2}\t{x3}\t{x4}\t{x1}')
elif x2<x1 and x2<x3 and x2<x4 and x1<x3 and x1<x4 and x3<x4:
	print(f'Numbers after condition: {x2}\t{x1}\t{x3}\t{x4}')
elif x2<x1 and x2<x3 and x2<x4 and x1<x3 and x1<x4 and x4<x3:
	print(f'Numbers after condition: {x2}\t{x1}\t{x4}\t{x3}')
elif x2<x1 and x2<x3 and x2<x4 and x4<x1 and x4<x3 and x1<x3:
	print(f'Numbers after condition: {x2}\t{x4}\t{x1}\t{x3}')
elif x2<x1 and x2<x3 and x2<x4 and x4<x1 and x4<x3 and x3<x1:
	print(f'Numbers after condition: {x2}\t{x4}\t{x3}\t{x1}')
elif x3<x1 and x3<x2 and x3<x4 and x1<x2 and x1<x4 and x2<x4:
	print(f'Numbers after condition: {x3}\t{x1}\t{x2}\t{x4}')
elif x3<x1 and x3<x2 and x3<x4 and x1<x2 and x1<x4 and x4<x2:
	print(f'Numbers after condition: {x3}\t{x1}\t{x24}\t{x2}')
elif x3<x1 and x3<x2 and x3<x4 and x2<x1 and x2<x4 and x1<x4:
	print(f'Numbers after condition: {x3}\t{x2}\t{x1}\t{x4}')
elif x3<x1 and x3<x2 and x3<x4 and x2<x1 and x2<x4 and x4<x1:
	print(f'Numbers after condition: {x3}\t{x2}\t{x4}\t{x1}')
elif x3<x1 and x3<x2 and x3<x4 and x4<x1 and x4<x2 and x1<x2:
	print(f'Numbers after condition: {x3}\t{x4}\t{x1}\t{x2}')
elif x3<x1 and x3<x2 and x3<x4 and x4<x1 and x4<x2 and x2<x1:
	print(f'Numbers after condition: {x3}\t{x4}\t{x1}\t{x2}')
elif x4<x1 and x4<x2 and x4<x3 and x1<x2 and x1<x3 and x2<x3:
	print(f'Numbers after condition: {x4}\t{x1}\t{x2}\t{x3}')
elif x4<x1 and x4<x2 and x4<x3 and x1<x2 and x1<x3 and x3<x2:
	print(f'Numbers after condition: {x4}\t{x1}\t{x3}\t{x2}')
elif x4<x1 and x4<x2 and x4<x3 and x2<x1 and x2<x3 and x1<x3:
	print(f'Numbers after condition: {x4}\t{x2}\t{x1}\t{x3}')
elif x4<x1 and x4<x2 and x4<x3 and x2<x1 and x2<x3 and x3<x1:
	print(f'Numbers after condition: {x4}\t{x2}\t{x3}\t{x1}')
elif x4<x1 and x4<x2 and x4<x3 and x3<x1 and x3<x2 and x1<x2:
	print(f'Numbers after condition: {x4}\t{x3}\t{x1}\t{x2}')
elif x4<x1 and x4<x2 and x4<x3 and x3<x1 and x3<x2 and x2<x1:
	print(f'Numbers after condition: {x4}\t{x3}\t{x2}\t{x1}')
