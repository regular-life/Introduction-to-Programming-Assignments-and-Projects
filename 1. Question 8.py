pryr=[50, 1450, 1400, 1700, 1500, 600, 1200]
q=0
for i in pryr:
    q+=i
t=0
x=0
c=0
while x>=c:
    k=0
    x=0
    c=0
    curyr=[]
    for i in pryr:
        c+=i
    for i in pryr:
        i+=i*(0.025-0.004*k-0.001*t)
        x+=i
        curyr=curyr+[i]
        k+=1
    pryr=curyr
    t+=1
print("The current total population is: ", x*10**6)
print("Years when maximum population is reached : " , t-1)
print("The total peak world population is : " , int(c*10**6))