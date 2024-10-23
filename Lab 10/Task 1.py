from random import *
def main ():
    length = 12
    x = [0] * length
    print('Monthly Sales: ',end='')
    for i in range (length):
        x[i] = randint(10,99)
        print(x[i],end=' ')
    print('\n')
    quarter = length//4
    a=max1=min1=max_average=min_average=p1=p2=p3=p4=0
    for j in range (4):
        max=min=sum=0
        print(f'Quarter {j+1}:',end='')
        for i in range (a,quarter):
            print(x[i],end=' ');sum += x[i]
            if i == 0:  max1=min1=x[i];p1=j+1;p2=j+1;
            elif x[i]>max1: max1=x[i];p1=j+1;
            elif x[i]<min1: min1=x[i];p2=j+1;
            if i == a:  max=min=x[i];
            elif x[i]>max:  max=x[i];
            elif x[i]<min:  min=x[i];
        avg = sum/3
        print(f'\tMin:{min}\tMax:{max}\tAverge:{avg:0.2f}')
        if j == 0:  max_average=min_average=avg;p3=j+1;p4=j+1;
        elif avg>max_average:     max_average=avg;p3=j+1;
        elif avg<min_average:   min_average=avg;p4=j+1;
        a = quarter
        quarter += 3
    print(f'Quarter {p2} has minimum sale {min1}')
    print(f'Quarter {p1} has maximun sale {max1}')
    print(f'Quarter {p4} has minimum average sale {min_average:0.2f}')
    print(f'Quarter {p3} has maximum average sale {max_average:0.2f}')
main()
