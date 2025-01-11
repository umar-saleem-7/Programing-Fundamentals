n = int(input("N: "))
a = n*2-2
for i in range (1,n):
    for j in range (n+1,i,-1):
        print('+',end='')
    for j in range (2,i*2):
        print(end=' ')
    for j in range (n+1,i,-1):
        print('+',end='')
    print()
print('+',end='')
for i in range (a):
    print(end=' ')
print('*')
for i  in range (2,n+1):
    for j in range (i):
        print('+',end='')
    for j in range (2,a):
        print(end=' ')
    for j in range (i):
        print('+',end='')
    print()
    a -= 2

