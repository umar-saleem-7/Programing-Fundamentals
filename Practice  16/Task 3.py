r = int(input('Rows :'))
i = 1
while i <= r:
    x = 1
    while x <= 26:
        print(chr(x+64),end='')
        x =x + 1
    i = i + 1
    print()

