allowance=20000
r=0.5
cost=int(input("Enter cost of the laptop : "))
t=int(input("Enter time limit : "))
print(cost*r/(100*allowance*(((1+(r/100))**t)-1)))