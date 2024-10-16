from random import *
def main():
    print('Roll No\tMid\tFinal\tSessional\tTotal\tGrade')
    i = 1
    c = 0
    oat = 0
    amm = 0
    asm = 0
    afm = 0
    mm = 0
    mmm = 0
    msm = 0
    mfm = 0
    mmo = 101
    mmmo = 36
    msmo = 26
    mfmo = 41
    while i <= 30:
        mid = randint(10,35)
        final = randint(10,40)
        sess = randint(10,25)
        t = mid + final + sess
        oat = oat + t
        amm = amm + mid
        asm = asm + sess
        afm = afm + final
        if t > mm:
            mm = t
        if mid > mmm:
            mmm = mid
        if sess > msm:
            msm = sess
        if final > mfm:
            mfm = final
        if t < mmo:
            mmo = t
        if mid < mmmo:
            mmmo = mid
        if sess < msmo:
            msno = sess
        if final < mfmo:
            mfmo = final
        if t > 90:
            g = 'A'
        elif t > 85:
            g = 'B+'
        elif t > 80:
            g = 'B'
        elif t > 75:
            g = 'B-'
        elif t > 70:
            g = 'C'
        elif t > 60:
            g = 'D'
        elif t > 50:
            g = 'E'
        elif t < 50:
            g = 'F'
            c = c + 1
        print(f'{i}\t{mid}\t{final}\t{sess}\t\t{t}\t{g}')
        i = i + 1
    print(f'Total:{30}')
    print('Pass:',30 - c)
    print('Fail:',c)
    ovl_avg_m = oat / 30
    avg_mid_m = amm / 30
    avg_sess_m = asm / 30
    avg_fin_m = afm / 30
    print(f'Overall average marks:\t\t{ovl_avg_m}')
    print(f'Average Midterm Marks:\t\t{avg_mid_m}')
    print(f'Average Sessional Marks:\t{avg_sess_m}')
    print(f'Average Final Marks:\t\t{avg_fin_m}')
    print(f'Maximum Marks:\t\t\t{mm}')
    print(f'Maximum Midterm Marks:\t\t{mmm}')
    print(f'Maximum Sessional Marks:\t{msm}')
    print(f'Maximum Final Marks:\t\t{mfm}')
    print(f'Minimum Marks:\t\t\t{mmo}')
    print(f'Minimum Midterm Marks:\t\t{mmmo}')
    print(f'Minimum Sessional Marks:\t{msmo}')
    print(f'Minimum Final Marks:\t\t{mfmo}')
    
main()
