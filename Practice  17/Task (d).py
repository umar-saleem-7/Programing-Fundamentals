r = int(input("Rows:"))
c = int(input("Columns:"))
i = 1
while i <= r:
    j = 1
    a = i
    while j <= c:
        print(a,end=' ')
        j = j + 1
        a = a + 1
    i = i + 1
    print()
