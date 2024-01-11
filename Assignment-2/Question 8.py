n=int(input())
f=open('Pages.txt','r')
f.seek(0,0)
d={}
init=[]
links=[]
t=f.readlines()
oi=[]
ans={}
for i in range(len(t)):
    init.append(float(t[i][7:10]))
    a=[]
    for j in range(len(t[i])-4):
        if t[i][j:j+3]=='URL':
            a.append(t[i][j:j+5])
    d[a[0]]=set(a[1:len(a)])
    links.append(len(set(a[1:len(a)])))
for i in range(len(t)):
    oi.append(init[i]/links[i])
k={}
j=0
for i in d.keys():
    k[i]=oi[j]
    j+=1
for i in d.keys():
    c=0
    for j in d.keys():
        if i!=j and i in d[j]:
            c+=k[j]
    ans[i]=c
print(d,ans)
po = sorted(ans.items(), key=lambda x:x[1])
print(po)
for i in range(1,n+1):
    print(po[-i][0])