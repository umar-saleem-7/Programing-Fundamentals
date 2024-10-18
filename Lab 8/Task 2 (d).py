def main():
    r = int(input("Rows :"))
    c = int(input("Columns :"))
    i = 1
    a = "*"
    while i <= r:
        j = 1
        while j <= c-1:
            print(a,end=' ')
            j = j + 1
        i = i + 1
        if j == c:
            print("*>")
main()
