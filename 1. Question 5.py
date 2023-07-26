def fact(x):
    f=1
    for i in range(2,x+1):
        f*=i
    return(f)
def sin(x):
    s=0
    for i in range(1,51):
        s+=(((-1)**(i+1))*(x**(2*i-1))/(fact(2*i-1)))
    return(s)
def cos(x):
    return((1-(sin(x)**2))**0.5)
def tan(x):
    return(sin(x)/cos(x))
x = float(input("Angle in degrees is : "))
b = float(input("Horizontal distance from the pole is : "))
x = 3.14*x/180
h=b*tan(x)
print("Height of the pole is : " , h)
print("Length of the line from the person to the top of the pole : " , (h**2 + b**2)**(0.5))