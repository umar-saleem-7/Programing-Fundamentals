def main():
    n1 = int(input('Enter 1st number :'))
    n2 = int(input('Enter 2nd number :'))
    n = 0
    count = 0
    if n1 < n2:
        while n1 <= n2:
            print(n1,end=' ')
            n =  n + n1
            n1 = n1 + 1
            count = count + 1
    elif n2 < n1:
        while n2 <= n1:
            print(n1,end=' ')
            n =  n + n1
            n1 = n1 - 1
            count =  count + 1
    print(f'\nSum : ',n)
main()
