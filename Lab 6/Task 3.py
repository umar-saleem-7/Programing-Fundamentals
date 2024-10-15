from random import *
def main ():
    i = 1
    marks = 0
    while i <= 10:
        x1 = randint(1,9)
        x2 = randint(1,9)
        print(f'N1:   {x1}   N2:   {x2}')
        sum = int(input('Enter sum :'))
        if sum == x1 + x2:
            marks = marks + 1
        else:
            sum = int(input('wrong,enter sum again :'))
            if sum == x1 + x2:
                marks = marks + 1
            else:
                sum = int(input('again wrong,enter sum again :'))
                if sum == x1 + x2:
                    marks = marks + 1
        difference = int(input('Enter difference :'))
        if difference == x1 - x2:
            marks = marks + 1
        else:
            difference = int(input('wrong,enter difference again :'))
            if difference == x1 - x2:
                marks = marks + 1
            else:
                difference = int(input('again wrong,enter difference again :'))
                if difference == x1 - x2:
                        marks = marks + 1
        product = int(input('Enter product :'))
        if product == x1 * x2:
            marks = marks + 1
        else:
            product = int(input('wrong,enter product again :'))
            if product == x1 * x2:
                marks = marks + 1
            else:
                product = int(input('again wrong,enter product again :'))
                if product == x1 * x2:
                    marks = marks + 1
        i = i + 1
    print('Obtained marks = ',marks)
main()
