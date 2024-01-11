a=float(input("Starting time : "))
b=float(input("Ending time : "))
import math
d=0
def v(t):
    if t==0:
        v=0
    else:
        v=2000*math.log(140000/(140000-2100*t)) -9.8*t
    return(v)
v1=v(0)
v2=v(a)
t=a
while t<=b:
    v1=v2
    v2=v(t+0.25)
    d+=0.25*(v1+v2)/2
    t+=0.25
print("Answer after integration : " , d)