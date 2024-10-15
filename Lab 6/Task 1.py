def main():
    a=0
    b=0
    x=0
    y=0
    i = 1
    while i <=99:
        if i > 9:
            a = i // 10
            b = i % 10
        c = a + b
        if c > 9:
            x = c // 10
            y = c % 10
        z = x + y
        if c == 0:
            print(f'[{i}]',end=' ')
        elif z == 0:
            print(f'[{i} {c}]',end=' ')
        else:
            print(f'[{i} {c} {z}]',end=' ')
        i = i + 1
main()
