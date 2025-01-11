r = int(input("Rows:"))
c = int(input("Columns:"))
for i in range (1,r+1):
    a = i
    for j in range (1,c+1):
        print(a,end=' ')
        a = a + 1
    print()
