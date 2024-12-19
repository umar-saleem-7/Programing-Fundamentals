def main():
    file = open('nums.txt','r')
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    i = 1
    while i <= 10000:
        n = int(file.readline())
        if n == 1:
            count1 = count1 + 1
        
        if n == 2:
            count2 = count2 + 1
        
        if n == 3:
            count3 = count3 + 1
        
        if n == 4:
            count4 = count4 + 1
        
        if n == 5:
            count5 = count5 + 1
        
        if n == 6:
            count6 = count6 + 1
        
        if n == 7:
            count7 = count7 + 1
        
        if n == 8:
            count8 = count8 + 1
        
        if n == 9:
            count9 = count9 + 1
        
        i = i + 1
    print('Count of 1 :',count1)
    print('Count of 2 :',count2)
    print('Count of 3 :',count3)
    print('Count of 4 :',count4)
    print('Count of 5 :',count5)
    print('Count of 6 :',count6)
    print('Count of 7 :',count7)
    print('Count of 8 :',count8)
    print('Count of 9 :',count9)
    file.close()
main()
