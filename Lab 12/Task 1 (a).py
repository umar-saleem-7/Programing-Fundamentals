from random import *
length=randint(5,9)
d=[[randint(1,9) for i in range (length)] for j in  range (length)]
for i in range (length):
    d[i][i]=0
for i in range (length):
    for j in range (length):
        print(d[i][j],end=' ')
    print()
def main(distance,city1,city2):
    print(f"Distance between city {city1} and city {city2}")
    print(f'Direct Distance: {d[city1][city2]}')
    print('Indirect Distance')
    for i in range (length):
        if i!=city1 and i != city2:
            print(f'Via city {i}: {d[city1][i]+d[i][city2]}')
main(d,2,4)
