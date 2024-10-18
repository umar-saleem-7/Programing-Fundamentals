i = 1
j = 1
r = int(input("Rows:"))
while i <= r:
    a = 1
    while a <= 4:
        print(chr(j+64),end=' ')
        j = j + 1
        a = a + 1
    i = i + 1
    print()
