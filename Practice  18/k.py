r = int(input("Rows:"))
c = int(input("Columns:"))
a = 1
for i in range (1,r+1):
    for j in range (1,c+1):
        print(i,end=' ')
    print()
    for j in range (1,c+1):
        print(chr(a+96),end=' ')
    a+=1
    print()

