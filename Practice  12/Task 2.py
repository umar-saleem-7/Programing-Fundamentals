def main():
    x = int(input(''))
    i = 1
    if x >26:
        print('Sorry, Integer is greater to print alphabets')
    else:
        while i <= x:
            print(chr(i + 64),end=' ')
            print(chr(123 - i),end=' ')
            i = i + 1
main()
