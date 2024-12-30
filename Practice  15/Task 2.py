def main():
    x = int(input('Enter Decimal Number :'))
    i = 1
    while x > 0:
        print(x % 8,end='')
        x = x // 8
main()
