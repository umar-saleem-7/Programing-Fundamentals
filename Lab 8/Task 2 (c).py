def main():
    r = int(input("Rows :"))
    a = "*"
    i = 1
    while i <= r:
        j = 1
        while j <= i:
            print(a,end=' ')
            j = j + 1
        i = i + 1
        print()
main()
