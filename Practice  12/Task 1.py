def main():
    x = int(input('Enter integer :'))
    i = 1
    a = 1
    if x >26:
        print('Sorry, Integer is greater to print alphabets')
    else:
        while i <=x:
            print(chr(i + 64),end='')
            i = i + 1
        print()
        while a <= x:
            print(chr(a + 96),end='')
            a = a + 1
main()
