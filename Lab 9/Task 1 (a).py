r = int(input("Rows: "))
a = 1
for k in range (r):
    for i in range (1,r+1):
        print(chr(a+64),end=' ')
        a = a + 1
        for j in range (1,i+1):
            print(j,end=' ')
    print()
