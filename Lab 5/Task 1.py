from random import *
def main():
    x = randint(20,99)
    a = x//10
    b = x%10
    print('Number ',x,' in English is',end=' ')
    if a == 2:
        print('twenty',end='')
    elif a == 3:
        print('thirty',end='')
    elif a == 4:
        print('forty',end='')
    elif a == 5:
        print('fifty',end='')
    elif a == 6:
        print('sixty',end='')
    elif a == 7:
        print('seventy',end='')
    elif a == 8:
        print('eighty',end='')
    elif a == 9:
        print('ninty',end='')
    if b ==1:
        print('-one')
    elif b == 2:
        print('-two')
    elif b == 3:
        print('-three')
    elif b == 4:
        print('-four')
    elif b == 5:
        print('-five')
    elif b == 6:
        print('-six')
    elif b == 7:
        print('-seven')
    elif b == 8:
        print('-eight')
    elif b == 9:
        print('-nine')
    elif b == 0:
        print()

main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
