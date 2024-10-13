a = int(input('Amount Deposit = '))
#122504.3
b = (a * 0.07) + a
c = (b * 0.07) + b
d = (c * 0.07) + c
x = (a * 0.1) + a
y = (x * 0.1) + x
z = (y * 0.1) + y
if a<=500000:
    print('Amount after one year = ',int(b))
    print('Amount after second year = ',int(c))
    print('Amount after third year = ',d)
else:
    print('Amount after one year = ',int(x))
    print('Amount after one year = ',int(y))
    print('Amount after one year = ',int(z))
