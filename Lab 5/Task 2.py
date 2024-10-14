from random import *
def main ():
    max = 0
    t1 = randint(1,4)
    if t1==1:
        type1 = 'D'
        color1 = 'RED'
    elif t1==2:
        type1 = 'H'
        color1 = 'RED'
    elif t1==3:
        type1 = 'S'
        color1 = 'BLACK'
    elif t1==4:
        type1 = 'C'
        color1 = 'BLACK'
    c1 = randint(1,13)
    print(f'Card 1 has value {c1} and its type is {type1}')
    t2 = randint(1,4)
    if t2==1:
        type2 = 'D'
        color2 = 'RED'
    elif t2==2:
        type2 = 'H'
        color2 = 'RED'
    elif t2==3:
        type2 = 'S'
        color2 = 'BLACK'
    elif t2==4:
        type2 = 'C'
        color2 = 'BLACK'
    c2 = randint(1,13)
    print(f'Card 2 has value {c2} and its type is {type2}')
    t3 = randint(1,4)
    if t3==1:
        type3 = 'D'
        color3 = 'RED'
    elif t3==2:
        type3 = 'H'
        color3 = 'RED'
    elif t3==3:
        type3 = 'S'
        color3 = 'BLACK'
    elif t3==4:
        type3 = 'C'
        color3 = 'BLACK'
    c3 = randint(1,13)
    print(f'Card 3 has value {c3} and its type is {type3}')



    if (c1 == c2 + 1 or c1 == c3 + 1) and (c2 == c1 + 1 or c2 == c3 + 1) and (c3 == c1 + 1 or c3 == c2 + 1) and t1 == t2 and t2 == t3:
        print('All cards are in sequence and of same type')
    elif c1 == c2 and c2 == c3 and t1 == t2 and t2 == t3:
        print('All cards have same number and of same type')
    elif t1 == t2 and t2 == t3:
        print('All cards have same type')
    elif color1 == color2 and color2 == color3:
        print('All cards have same color')
    elif (c1 == c2 + 1 or c1 == c3 + 1) and (c2 == c1 + 1 or c2 == c3 + 1) and (c3 == c1 + 1 or c3 == c2 + 1):
        print('All cards are in sequence')
    elif t1 ==t2 or t1 == t3 or t2 == t3:
        print('Two cards have same type')
    elif (c1 == c2 + 1 or c1 == c3 + 1) or (c2 == c1 + 1 or c2 == c3 + 1) or (c3 == c1 + 1 or c3 == c2 + 1):
        print('Two carsd are in sequence')
    else:
        if max < c1:
            max = c1
        if max < c2:
            max = c2
        if max < c3:
            max = c3
        print('Highest value of card is :',max)
main()
main()
main()
main()
main()
