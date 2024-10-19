r = int(input("Rows: "))
c = int(input("Columns: "))
for i in range (1,r+1):
    sum = 0
    a = 1
    for j in range (1,c+1):
        print(a,end='')
        sum = sum + a
        a = a + i
        if j != c:
            print('+',end='')
    print('=',sum)
