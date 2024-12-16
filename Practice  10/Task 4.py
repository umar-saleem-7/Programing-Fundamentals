#from random import *
def main():
    max = 0
    i = 1
    while i<=5:
        x = int(input('Enter number :'))
        #x = randint(1,100000)     #for random numbers
        #print()
        if x > max:
            max = x
        i = i + 1
    print('Max Number :',max)    
main()
