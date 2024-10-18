file = open("Players.txt","r")
i = 1
best_avg = 0
bc = 0  #position of best average
hr = 0  #highest run
number_of_players = int(file.readline())
print('Number os players :',number_of_players)
while i <= number_of_players:
    j = 1
    match_played = int(file.readline())
    print(f'Players {i} :',end= ' ')
    sum = 0
    c = 1   #count
    max = 0
    while j <= match_played:
        n = int(file.readline())
        print(n,end=' ')
        sum = sum + n
        if n > max:
            max = n
        c = c + 1
        j = j +  1
        if n > hr:
            hr = n
    print('        \t\tAverage : ',(sum)//(c-1),end=' ')
    print('\tMax :',max)
    if (sum)//(c-1) > best_avg:
        best_avg = (sum)//(c-1)
        bc = i
    i = i + 1
print(f'Player {bc} has best average')
print(f'The Highest runs are {hr}')
file.close()
