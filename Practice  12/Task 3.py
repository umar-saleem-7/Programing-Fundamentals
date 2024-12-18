def main():
    x = int(input(''))
    i = 1
    while i <= x:
        if x % 2 == 0:
            print(i,end=' ')
            i = i + 1
        else:
            while i <= x:
                print(x,end=' ')
                x = x - 1
            i = i + 1
main()
print()
main()
