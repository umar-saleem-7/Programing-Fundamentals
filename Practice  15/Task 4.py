from random import *
def main():
    i = 1
    min = 1000
    c_min = 0
    max = 0
    c_max = 0
    min_element = 0
    max_element = 0
    while i <= 10:
        n1 =  randint(1,100)
        n2 =  randint(1,100)
        n3 =  randint(1,100)
        print(f'set {i} = {n1} {n2} {n3}',end='          \t')
        avg = (n1+n2+n3)/3
        print('Average :',avg)
        if avg < min:
            min = avg
            c_min = i
            min_element = n1,n2,n3

        if max < avg:
            max = avg
            c_max = i
            max_element = n1,n2,n3

        i = i + 1
    print('\n')
    print(f'set {c_min} : {min_element} has minimun average = {min}')
    print(f'set {c_max} : {max_element} has maximum average = {max}')
main()
