x = int(input('Enter three-digit Number :'))
a = x //100
b = (x%100)//10
c = x%10
s = a + b + c
print(f'Sum of digits :{s}')