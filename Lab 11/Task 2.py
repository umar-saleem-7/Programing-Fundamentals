from random import *
def main ():
    length = 30
    SEN = -1
    list1 = [0] * length
    list2 = [0] * length
    for i in range (length):
        list1[i] = randint(0,100)
        list2[i] = i+1
        print(list1[i],end=' ')
    print()
    l = randint(3,5)        #length to remove 3 to 5 elements from a roll no list
    for i in range(l):
        x = randint (1,30)
        for j in range (length):
            if x == list2[j]:
                list2[j]=SEN
    count = 0
    print(f'Roll No\tMarks')
    for i in range (length):
        if list2[i]>0:
            print(f'{list2[i]}\t\t{list1[i]}')
            count += 1
    list3 = [0] * count
    list4 = [0] * count
    j=0
    for i in range (length):
        if list2[i]>0:
            list3[j]=list1[i]
            list4[j]=list2[i]
            j += 1
    print(list3)
    print(list4)
main()
