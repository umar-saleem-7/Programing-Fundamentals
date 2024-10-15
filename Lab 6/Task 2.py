from random import *
def main():
    i = 1
    while i<=100:
        a = int(i/10)
        b =i%10
        if a == 2:
            print('twenty',end=' ')
        elif a == 3:
            print('thirty',end=' ')
        elif a == 4:
            print('forty',end=' ')
        elif a == 5:
            print('fifty',end=' ')
        elif a == 6:
            print('sixty',end=' ')
        elif a == 7:
            print('seventy',end=' ')
        elif a == 8:
            print('eighty',end=' ')
        elif a == 9:
            print('ninty',end=' ')
        if i == 10:
            print('ten')
        elif i == 11:
            print('eleven')
        elif i == 12:
            print('twelve')
        elif i == 13:
            print('thirteen')
        elif i == 14:
            print('forteen')
        elif i == 15:
            print('fifteen')
        elif i == 16:
            print('sixteen')
        elif i == 17:
            print('seventeen')
        elif i == 18:
            print('eighteen')
        elif i == 19:
            print('nineteen')
        elif i == 100:
            print('hundred')
        elif b == 1:
            print('one')
        elif b == 2:
            print('two')
        elif b == 3:
            print('three')
        elif b == 4:
            print('four')
        elif b == 5:
            print('five')
        elif b == 6:
            print('six')
        elif b == 7:
            print('seven')
        elif b == 8:
            print('eight')
        elif b == 9:
            print('nine')

        elif b == 0:
            print()

        i = i + 1
main()
