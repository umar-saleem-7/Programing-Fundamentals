x = int(input("N: "))
y = int(input("K: "))
i = 1
print('{',end='')
while i <= x:
    j = 1
    while j <= y:
        print(f'({i},{j})',end='')
        if i < x or j < y:
            print(',',end='')
        j = j + 1
    i = i + 1
print('}')
