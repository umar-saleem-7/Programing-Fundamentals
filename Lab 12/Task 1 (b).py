from random import *
length=randint(5,9)
d=[[randint(1,9) for i in range (length)] for j in  range (length)]
for i in range (length):
    d[i][i]=0
for i in range (length):
    for j in range (length):
        print(d[i][j],end=' ')
    print()
def main():
    for j in range(1,length):
        # print(city1,city2)
        # print(f'Direct Distance: {d[city1][city2]}')
        temp1=d[0][j];temp2=1654294981981;p=0;
        # print('Indirect Distance')
        for i in range (length):
            if i!=0 and i != j:
                # print(f'Via city {i}: {d[city1][i]+d[i][city2]}')
                if temp2>d[0][i]+d[i][j]:
                    temp2=d[0][i]+d[i][j]
                    p=i
        if temp1<temp2:
            print(f'Shortest Distance betweem city {0} and city {j} is {temp1}')
        else:
            print(f'Shortest Distance betweem city {0} and city {j} is {temp2} via city {p}')
main()
