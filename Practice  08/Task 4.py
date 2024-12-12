def main():
    x = input('Enter character :')
    y = int(input('Enter bit position :')) 
    a = ord(x)
    z = 2 ** (y - 1)
    if (a & z) == z:
        print(f'The bit Number {y} is on in {x}')
    else:
        print(f'The bit Number {y} is off in {x}')

main()
main()
