def f(x):
    return(x**3 - 10.5*x**2 + 34.5*x - 35)
def f1(x):
    return(3*x**2 - 21*x + 34.5)
x0=float(input("Input the value of x0 here : "))
x=x0
for i in range(100):
    if -0.2 <= f(x) <= 0.2 :
        t=x
        flag=True
        break
    else :
        x = (f1(x)*x - f(x))/f1(x)
        flag=False
        continue
if flag :
    print("The root of the equation found after Newton-Raphson method is : " , t)
else:
    print("Couldn't find any solution.")