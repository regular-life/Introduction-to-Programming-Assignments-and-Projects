n=0
x=int(input("Enter x0 : "))
y=int(input("Enter y0 : "))
x0=x
y0=y
d=0
flag=True
while flag :
    n=int(input("Enter distance to travel : "))
    if 0<n<=25:
        y+=n
        d+=n
    elif 25<n<51:
        y-=n
        d+=n
    elif 50<n<76:
        x+=n
        d+=n
    elif n>=76:
        x-=n
        d+=n
    elif n<=0:
        flag=False
print("The coordinates are : ",x,y)
print("The total distance travelled is : " , d)
print("The straight line distane between Starting and Ending points is : " , ((x-x0)**2 + (y-y0)**2)**(0.5))