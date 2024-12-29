def main ():
    i = 65
    while i <= 90:
        x = chr(i)
        if x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
            print()
            print(f'{x}')
        elif x != 'A' or x != 'E' or x != 'I' or x != 'O' or x != 'U':
            print(x,end='')
        i = i + 1
main()
