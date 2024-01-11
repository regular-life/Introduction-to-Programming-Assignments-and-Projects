f=open("Q3.txt","r")
f.seek(0,0)
t=f.readlines()
n=int(len(t)**0.5)
ans=[0]*n
j=0
for i in range(n):
    j+=1
    while j<len(t) and t[j][-2].isnumeric():
        ans[i]+=int(t[j][-2])
        j+=1
M=max(ans)
m=min(ans)
a=[]
b=[]
for i in range(len(ans)):
    if ans[i]==M:
        a.append(t[4*i][0:len(t[4*i])-2])
    elif ans[i]==m:
        b.append(t[4*i][0:len(t[4*i])-2])
print("Person(s) with maximum signature : " , *a)
print("Person(s) with minimum signature : " , *b)