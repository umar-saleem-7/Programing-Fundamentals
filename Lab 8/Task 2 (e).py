def main ():
    r = int(input("Rows :"))
    i = 1
    sum = 0
    c = 5
    while i <= r:
        j = 1
        while j <= c:
            print(j,end=' ')
            sum = sum + j
            j = j + 1
        i = i + 1
        c = c + 1
        print(f"= {sum}")
        sum = 0
main()
