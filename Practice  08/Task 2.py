x = input('Enter first chracter :')
y = input('Enter second chracter :')
a = ord(x)
b = ord(y)
i = 0
if (a & 1) == (b & 1):
	i = i+1
if (a & 2) == (b & 2):
	i = i+1
if (a & 4) == (b & 4):
	i = i+1
if (a & 8) == (b & 8):
	i = i+1
if (a & 16) == (b & 16):
	i = i+1
if (a & 32) == (b & 32):
	i = i+1
if (a & 64) == (b & 64):
	i = i+1
if (a & 128) == (b & 128):
	i = i+1
if (a & 256) == (b & 256):
	i = i+1
print(f'In {x} and {y}, {i} bit(s) are same')
