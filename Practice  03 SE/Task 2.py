eng = int(input ('Enter eng marks'))
urdu = int(input ('Enter urdu marks'))
maths = int(input ('Enter maths marks'))
isl = int(input ('Enter isl marks'))
pakstudies = int(input ('Enter pakstudies marks'))
phy = int(input ('Enter phy marks'))
che = int(input ('Enter che marks'))
bio = int(input ('Enter bio marks'))

Total = eng + urdu + maths + isl + pakstudies + phy + che + bio

print('Subject   \tTotal\tObtained')
print('1. English   \t75\t',eng)
print('2. Urdu   \t75\t',urdu)
print('3. Maths   \t75\t',maths)
print('4. islamiat   \t50\t',isl)
print('5. Pak Studie\t50\t',pakstudies)
print('6. Physics   \t75\t',phy)
print('7. Chemistry   \t75\t',che)
print('8. Biology   \t75\t',bio)
print('   TOTAL \t525\t',Total)

print('Percentage Marks : ',Total/525*100)

merit = int(input('\nEnter Last Year Merit of GC:'))
print('Marks Required in tenth:',merit - Total)
