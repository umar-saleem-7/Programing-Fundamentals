from random import *
def main():
    i = 1
    while i <= 10:
        x = randint(65,90)
        y = chr(x)
        if y == 'A' or y == 'E' or y == 'I' or y == 'O' or y == 'U':
            print(f'Alphabet {y} is Vowel')
        else:
            print(f'Alphabet {y} is Consonant')
        i = i + 1
main()
