from random import *
def main():
    i = 1
    while i <= 10:
        x = randint(1,100)
        y = x % 10
        c = x//10
        print(f'Number in digit is {x}',end=' ')
        print(' and  Number in words is ',end=' ')
        if c == 2:
            print('twenty',end=' ')
        elif c == 3:
            print('thirty',end=' ')
        elif c == 4:
            print('forty',end=' ')
        elif c == 5:
            print('fifty',end=' ')
        elif c == 6:
            print('sixty',end=' ')
        elif c == 7:
            print('seventy',end=' ')
        elif c == 8:
            print('eighty',end=' ')
        elif c == 9:
            print('ninety',end=' ')
        if x == 11:
            print('eleven')
        elif x == 12:
            print('twelve')
        elif x == 13:
            print('thirteen')
        elif x == 14:
            print('forthteen')
        elif x == 15:
            print('fifteen')
        elif x == 16:
            print('sixteen')
        elif x == 17:
            print('seventeen')
        elif x == 18:
            print('eighteen')
        elif x == 19:
            print('ninteen')
        elif x == 10:
            print('ten',end='\n')
        elif x == 100:
            print('hundred',end='\n')
        elif y == 1:
            print('one')
        elif y == 2:
            print('two')
        elif y == 3:
            print('three')
        elif y == 4:
            print('four')
        elif y == 5:
            print('five')  
        elif y == 6:
            print('six')
        elif y == 7:
            print('seven')
        elif y == 8:
            print('eight')
        elif y == 9:
            print('nine')
        elif y == 0:
            print()

        i = i + 1

     
main()

