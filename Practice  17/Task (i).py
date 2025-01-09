r = int(input("Rows:"))
c = int(input("Columns:"))
i = 1
while i <= r:
    j = 1
    while j <= c:
        print(i,end=' ')
        j = j + 1
    print()
    k = 1
    while k <= c:
        print(chr(i + 96),end= ' ')
        k = k + 1
    i = i + 1
    print()
