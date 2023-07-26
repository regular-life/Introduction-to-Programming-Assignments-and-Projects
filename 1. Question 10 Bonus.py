def f(x):
    return(x**3 - 10.5*x**2 + 34.5*x - 35)
def f1(x):
    return(3*x**2 - 21*x + 34.5)
n=int(input())
x1=int(input())
x2=int(input())
x=x1
arr=[]
for i in range(n):
    for i in range(100):
        if -0.2 <= f(x) <= 0.2 :
            t=x
            flag=True
            break
        else :
            x = (f1(x)*x - f(x))/f1(x)
            flag=False
            continue
    arr.append(t)
    x+=1
print(arr)