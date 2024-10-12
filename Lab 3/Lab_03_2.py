amount = int (input ('Amount Deposited = '))
a = int((amount * 0.1)+amount)
b = int(a * 0.1 )+ a
c = int(b * 0.1)+ b
print ('Amount after one year = ', a)
print ('Amount after second year = ', b)
print ('Amount after third year = ',  c)
