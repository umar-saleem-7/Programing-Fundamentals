from random import *

x1 = randint(1,1000)
x2 = randint(1,1000)
x3 = randint(1,1000)
print(f'Numbers before condition: {x1}\t{x2}  \t{x3}')
if x1<x2 and x1<x3 and x2<x3:
    print(f'Numbers after condition: {x1}  \t{x2}  \t{x3}')
elif x1<x2 and x1<x3 and x3<x2:
    print(f'Numbers after condition: {x1}  \t{x3}  \t{x2}')
elif x2<x1 and x2<x3 and x1<x3:
    print(f'Numbers after condition: {x2}  \t{x1}  \t{x3}')
elif x2<x1 and x2<x3 and x3<x1:
    print(f'Numbers after condition: {x2}  \t{x3}  \t{x1}')
elif x3<x1 and x3<x2 and x1<x2:
    print(f'Numbers after condition: {x3}  \t{x1}  \t{x2}')
elif x3<x1 and x3<x2 and x2<x1:
    print(f'Numbers after condition: {x3}  \t{x2}  \t{x1}')