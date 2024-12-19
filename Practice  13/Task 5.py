def main():
    file = open('letters.txt','r')
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_f = 0
    count_g = 0
    count_h = 0
    count_i = 0
    count_j = 0
    count_k = 0
    count_l = 0
    count_m = 0
    count_n = 0
    count_o = 0
    count_p = 0
    count_q = 0
    count_r = 0
    count_s = 0
    count_t = 0
    count_u = 0
    count_v = 0
    count_w = 0
    count_x = 0
    count_y = 0
    count_z = 0
    i = 1
    while i <= 10000:
        n = (file.readline().strip('\n'))
        if n == 'A' or n == 'a':
            count_a = count_a + 1
        if n == 'B' or n == 'b':
            count_b = count_b + 1
        if n == 'C' or n == 'c':
            count_c = count_c + 1
        if n == 'D' or n == 'd':
            count_d = count_d + 1
        if n == 'E' or n == 'e':
            count_e = count_e + 1
        if n == 'F' or n == 'F':
            count_f = count_f + 1
        if n == 'G' or n == 'g':
            count_g = count_g + 1
        if n == 'H' or n == 'h':
            count_h = count_h + 1
        if n == 'I' or n == 'i':
            count_i = count_i + 1
        if n == 'J' or n == 'j':
            count_j = count_j + 1
        if n == 'K' or n == 'k':
            count_k = count_k + 1
        if n == 'L' or n == 'l':
            count_l = count_l + 1
        if n == 'M' or n == 'm':
            count_m = count_m + 1
        if n == 'N' or n == 'n':
            count_n = count_n + 1
        if n == 'O' or n == 'o':
            count_o = count_o + 1
        if n == 'P' or n == 'p':
            count_p = count_p + 1
        if n == 'Q' or n == 'q':
            count_q = count_q + 1
        if n == 'R' or n == 'r':
            count_r = count_r + 1
        if n == 'S' or n == 's':
            count_s = count_s + 1
        if n == 'T' or n == 't':
            count_t = count_t + 1
        if n == 'U' or n == 'u':
            count_u = count_u + 1
        if n == 'V' or n == 'v':
            count_v = count_v + 1
        if n == 'W' or n == 'w':
            count_w = count_w + 1
        if n == 'X' or n == 'x':
            count_x = count_x + 1
        if n == 'Y' or n == 'y':
            count_y = count_y + 1
        if n == 'Z' or n == 'z':
            count_z = count_z + 1
            
        i = i + 1
    print(f'Count of A : {count_a}')
    print(f'Count of B : {count_b}')
    print(f'Count of C : {count_c}')
    print(f'Count of D : {count_d}')
    print(f'Count of E : {count_e}')
    print(f'Count of F : {count_f}')
    print(f'Count of G : {count_g}')
    print(f'Count of H : {count_h}')
    print(f'Count of I : {count_i}')
    print(f'Count of J : {count_j}')
    print(f'Count of K : {count_k}')
    print(f'Count of L : {count_l}')
    print(f'Count of M : {count_m}')
    print(f'Count of N : {count_n}')
    print(f'Count of O : {count_o}')
    print(f'Count of P : {count_p}')
    print(f'Count of Q : {count_q}')
    print(f'Count of R : {count_r}')
    print(f'Count of S : {count_s}')
    print(f'Count of T : {count_t}')
    print(f'Count of U : {count_u}')
    print(f'Count of V : {count_v}')
    print(f'Count of W : {count_w}')
    print(f'Count of X : {count_x}')
    print(f'Count of Y : {count_y}')
    print(f'Count of Z : {count_z}')

    file.close()
main()
