a = int(input('Enter milk cost:'))
b = int(input('Enter sugar cost:'))
c = int(input('Enter tea cost:'))
d = int(input('Enter biscuits cost:'))
print('Previous month budget')
print(f'Milk:\t\t{a}')
print(f'Sugar:\t\t{b}')
print(f'Tea:\t\t{c}')
print(f'Biscuits:\t{d}\n\n')
x = int((a*0.2)+a)
y = int((b*0.2)+b)
z = int((c*0.2)+c)
t = int((d*0.2)+d)
print('Next month budget')
print(f'Milk:\t\t{x}')
print(f'Sugar:\t\t{y}')
print(f'Tea:\t\t{z}')
print(f'Biscuits:\t{t}')
total = x + y + z +t
print('----------------------------')
print(f'Total:\t\t{total}')
