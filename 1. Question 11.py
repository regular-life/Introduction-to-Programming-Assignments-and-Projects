#Number converter
#This program can convert any given number to it's decimal counterpart and thereafter to number with any base of the user's choice.

#Conversion to Decimal
N=input("The number to convert : ")
B=int(input("The base of the given number : "))
s=0
l=len(N)
for i in N:
    if i==".":
        d=N.index(".")
        break
    else:
        d=l+1
perf=N[:d]
frac=N[-(l-d)+1::]
l1=len(perf)
l2=len(frac)
'''Converts number before decimal place'''
for i in perf:
    if i.isalpha():
        s+=(ord(i)-55)*(B**(l1-perf.index(i)-1))
    else:
        s+=(int(i)*(B**(l1-perf.index(i)-1)))
'''Converts number after decimal place'''
for i in frac:
    if i.isalpha():
        s+=(ord(i)-55)*(B**(-(frac.index(i)+1)))
    else:
        s+=(int(i)*(B**(-(frac.index(i)+1))))
        
#Conversion to any base according to user's input
n=s
b=int(input("Enter base to convert to : "))
x=int(n)
y=n-x
'''Converts number before decimal place'''
def perf(n,b):
    q=1
    s=[]
    while q!=0:
        q=n//b
        r=n%b
        n=q
        if r<10:
            s=s+[r]
        else:
            s=s+[chr(55+r)] 
    ans=[]    
    for i in s:
        ans=[i]+ans       
    k=''   
    for i in ans:
        k+=str(i)
    return(k)
'''Converts number after decimal place'''
def dec(n,b):
    f=1
    s=[]    
    while f!=0:
        f=n*b-int(n*b)
        if f<10:
            s=s+[int(n*b)]
        else:
            s=s+[chr(55+int(n*b))]
        n=f        
    k=''    
    for i in s:
        k+=str(i)
    return(k)

o=int(perf(x,b))
u=len(str(dec(y,b)))
v=(int(dec(y,b)))/(10**u)

print("The number in decimal system is : " , s)
if y!=0:
    print("The number after conversion is : ", o+v)
else:
    print("The number after conversion is : ", o)