n = int(input("N: "))
for i in range (1,n):
    a = 1
    for j in range (1,n+2):
        print(chr(a+96),end=' ')
        a = a + i
    print()
