allowance=20000
sf=0.1
r=0.5
cost=int(input("Enter cost of the laptop : "))
p=sf*allowance
p0=sf*allowance
t=1
flag=True
while flag :
    if p<cost :
        t+=1
        p=p0+(p*(1+(r/100)))
        flag=True
    else:
        flag=False
        print("Months after which you will be able to but the laptop : " , t)
        print("Amount of savings that will remain after purchase : " , p-cost)