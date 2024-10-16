from random import *
def main():
    count = 0
    ans1 = 0
    ans2 = 0
    ans3 = 0
    i = 1
    while i <= 10:
        n = randint(1,3)
        if n == 1:
            n1 = randint(0,99)
            n2 = randint(0,99)
            print(f'1:Addition \n N1 : {n1}  N2 : {n2}')
            x = int(input('Enter Addition :'))
            if x == (n1 + n2):
                print('Correct')
                count = count + 1
            else:
                print('Incorrect')
        if n == 2:
            n1 = randint(10,99)
            n2 = randint(10,n1-1)
            print(f'2:Subtraction \n  N1 : {n1}  N2 : {n2}')
            y = int(input('Enter Subtraction :'))
            if y == (n1 - n2):
                print('Correct')
                count = count + 1
            else:
                print('Incorrect')
        if n == 3:
            n1 = randint(0,9)
            n2 = randint(0,9)
            print(f'3:Multiplication \n N1 : {n1}  N2 : {n2}')
            z = int(input('Enter Multiplication :'))
            if z == (n1 * n2):
                print('Correct')
                count = count + 1
            else:
                print('Incorrect')
        i = i + 1
    print(f'Score :  {count} out of 10')
main()
