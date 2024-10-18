def main():
    r = int(input("Rows :"))
    c = int(input("Columns :"))
    i = 1
    a = "*"
    while i <= r:
        j = 1
        while j <= c:
            print("*",end=' ')
            a = a + "*"
            j = j + 1
        i = i + 1
        print()
main()
