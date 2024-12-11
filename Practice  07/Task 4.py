x = int(input('Mark 1:'))
y = int(input('Mark 2:'))
#print('Mark 1: ',x)
#print('Mark 2: ',y)
a = abs(x - y)
if x == y:
    print('SAME')
elif x >= 85 and x<100 and y >=85 and y<100:
    print('ALMOST SAME')
elif x >= 80 and x<85 and y >=80 and y<85:
    print('ALMOST SAME')
elif x >= 75 and x<80 and y >=75 and y<80:
    print('ALMOST SAME')
elif x >= 70 and x<75 and y >=70 and y<75:
    print('ALMOST SAME')
elif x >= 65 and x<70 and y >=65 and y<70:
    print('ALMOST SAME')
elif x >= 61 and x<65 and y >=61 and y<65:
    print('ALMOST SAME')
elif x >= 58 and x<61 and y >=58 and y<61:
    print('ALMOST SAME')
elif x >= 55 and x<58 and y >=55 and y<58:
    print('ALMOST SAME')
elif x >= 50 and x<55 and y >=50 and y<55:
    print('ALMOST SAME')
elif x<50 and y<50:
    print('ALMOST SAME')
else:
    print('DIFFERENT')
