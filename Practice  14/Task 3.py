def main():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print(end='')
        elif i % 3 == 0 or i % 5 == 0:
            print(i,end=' ')
        i = i + 1
main()
