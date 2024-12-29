def main():
    i = 1
    count = 0
    while i <= 100:
        print(i,end=' ')
        count = count + 1
        if count == 5:
            count = 0
            print()
        i = i + 1
main()
