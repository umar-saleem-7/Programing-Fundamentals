n = int(input("Rows: "))
a = n*2-1
for i in range (n):
    for j in range(i):
        print(' ',end='')
    print('|_',end='')
    for j in range (a-1):
        print(' ',end='')
    if i != n-1:
        print('_|')
    else:
        print('|')
    a = a - 2
