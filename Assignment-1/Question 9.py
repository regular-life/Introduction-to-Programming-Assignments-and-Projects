def d(p):
	return(2.718**(10-1.05*p))
def s(p):
	return(2.718**(1+1.06*p))
x=1
flag=True
while flag==True:
    if (d(x)-s(x)) < 0.0000001:
        flag=False
        print("The equilibrium price is : ", x)
        print("Demand at equilibrium : " , d(x))
        print("Supply at equilibrium : " , s(x))
    else:
        x*=1.05
if flag==True:
    print("No equilibrium found.")