from random import *
def main ():
    length = 10
    x = [0] * length
    y = [0] * length
    z = [0] * length
    ans = [0] * length
    score =0
    for i in range (length):
        x[i] = randint(1,9)
        y[i] = randint(1,9)
    for i in range (length):
        z[i] = x[i]+y[i]
    for i in range (length):
        print(f'{x[i]} + {y[i]} = ',end='')
        ans[i] = int(input())
        if ans[i] == z[i]:      score += 1
    print(f'Score  {score}/{length}')
    if score!=length:
        print(f'Incorrect\t\tCorrect')
    for i in range (length):
        if ans[i] != z[i]:
            print(f'{x[i]} + {y[i]} = {ans[i]}\t\t{x[i]} + {y[i]} = {z[i]}')
main()
