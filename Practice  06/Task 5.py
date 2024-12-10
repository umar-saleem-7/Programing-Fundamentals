x1 = int(input('width of first rectangle:'))
y1 = int(input('length of first rectangle:'))
x2 = int(input('width of second rectangle:'))
y2 = int(input('length of second rectangle:'))
a1 = x1 * y1
a2 = x2 * y2
if a1>a2:
    print(f'Result: second rectangle is smaller')
else:
    print(f'Result: first rectangle is smaller')