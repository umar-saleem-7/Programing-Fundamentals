def main():
    a = input('Enter character :')
    print('Character :',a)
    x = ord (a)
    if x & 1 == 0:
        x = x | 1
    else:
        x = x & ~1
    if x & 2 == 0:
        x = x | 2
    else:
        x = x & ~2
    if x & 4 == 0:
        x = x | 4
    else:
        x = x & ~4
    if x & 8 == 0:
        x = x | 8
    else:
        x = x & ~8
    if x & 16 == 0:
        x = x | 16
    else:
        x = x & ~16
    if x & 32 == 0:
        x = x | 32
    else:
        x = x & ~32
    b = chr(x)
    print('Character after Flip :',b)
main()
main()
