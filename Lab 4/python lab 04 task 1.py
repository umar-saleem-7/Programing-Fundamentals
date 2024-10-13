x = int(input('basic salary='))
g = x + (x * 0.1) + (x * 0.15) +(x * 0.45)
a = 12 * g      #g = (x + (x * 0.1) + (x * 0.15) +(x * 0.45))
if a<=200000:
    t = g * 0
if a>400000 and a<=600000:
    t = g * 0.1
if a>600000 and a<=800000:
    t = g * 0.2
if a>800000:
    t = g * 0.25
Tax = t
netsalary = g - t
print('Basic Salary     \t',x)
print('Medical Allowance   \t',int(x*0.1))
print('Conveyance Allowance  ',int(x * 0.15))
print('House rent       \t',int(x * 0.45))
print('-----------------------------')
print('Gross Salary\t\t',int(g))
print('Less Tax  \t\t',int(Tax))
print('-----------------------------')
print('Net Salary \t\t',int(netsalary))
print('-----------------------------')
