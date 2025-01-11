r = int(input("Rows:"))
c = int(input("Columns:"))
for i in range (1,r+1):
    for j in range (1,c+1):
        print(j,end=' ')
    print()
    a = i
    for j in range (1,c+1):
        print(chr(a+96),end=' ')
        a+=1
    print()

