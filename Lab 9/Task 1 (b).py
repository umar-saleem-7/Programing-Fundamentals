n = int(input("N: "))
a = n*2-2
for i in range (n):
    for j in range (i):
        print(' ',end='')
    print('*',end='')
    for j in range (a-1):
        print(' ',end='')
    if i != n-1:
        print('*',end='')
    for j in range (i*2-1):
        print(' ',end='')
    if i != 0:
        print('*',end='')
    for j in range (a-1):
        print(' ',end='')
    if i != n-1:
        print('*')
    a = a - 2
print()
