r = int(input('Rows :'))
c = int(input('Columns :'))
i = 1
while i <= r:
    a = 1
    while a <= c:
        print('*',end=' ')
        a = a + 1
    i = i + 1
    print()
