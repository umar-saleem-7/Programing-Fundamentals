eggs = int(input('Enter number of eggs :'))
x = eggs//6
y = eggs%6
if y>0:
    print('packs\t:',x+1)
else:
    print('packs\t:',x)
