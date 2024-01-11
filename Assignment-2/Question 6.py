wts = [(10, 5), (10, 5), (100, 15), (40, 10), (100,15), (10,5), (80,20), (100,25)]
f=open("IPMarks.txt","r")
f.seek(0,0)
z=open("IPGrades.txt", "w")
z.seek(0,0)
t=f.readlines()
for i in t:
    a=i.index(' ')
    q=i[a+1:len(i)]
    q=q.split(',')
    q[len(q)-1]=q[len(q)-1][0:len(q[len(q)-1])-1]
    k=i[0:a-1]
    p=0
    for i in range(len(q)):
        p+=int(int(q[i])*wts[i][1]/wts[i][0])
    k+=' '
    k+=str(p)
    k+=' '
    if p>=80:
        k+='A'
    elif 70<=p<80:
        k+='A-'
    elif 60<=p<70:
        k+='B'
    elif 50<=p<60:
        k+='B-'
    elif 40<=p<50:
        k+='C'
    elif 35<=p<40:
        k+='C-'
    elif 30<=p<35:
        k+='D'
    else:
        k+='F'
    z.write(k)
    z.write('\n')