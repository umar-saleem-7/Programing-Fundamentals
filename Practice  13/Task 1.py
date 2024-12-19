def main():
    file = open('nums.txt','r')
    i = 1
    x = 0
    while i <= 10000:
        n = int(file.readline())
        x = x + n
        i = i + 1
    avg = x / 10000
    print('Average',avg)
    file.close()
main()
