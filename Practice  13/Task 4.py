def main():
    file = open('counts.txt','r')
    sum = 0
    i = 1
    while i < 10:
        n = int(file.readline())
        sum = sum + n
        i = i + 1
    print('SUM =',sum)
    if sum == 10000:
        print('Yes,It is equal to 10000')
    else:
        print('Not equal')
main()
