r = int(input("Rows: "))
c = int(input("Columns: "))
i = 1
a = 1
b = 1
while i <= r:
    j = 1
    a = i
    while j <= c:
        print(a,end=' ')
        j = j + 1
        a = a + 1
    print()
    k = 1
    b = i
    while k <= c:
        print(chr(b + 96),end= ' ')
        k = k + 1
        b = b + 1
    i = i + 1
    print()
