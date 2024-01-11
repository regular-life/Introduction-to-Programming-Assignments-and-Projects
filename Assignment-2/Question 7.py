f=open('Addrbook.txt','r')
f.seek(0,0)
t=f.readlines()
d={}
name=[]
phone=[]
address=[]
mail=[]
def fn(d):
    myKeys = list(d.keys())
    myKeys.sort()
    sorted_dict={i: d[i] for i in myKeys}
    return(sorted_dict)
for i in range(len(t)):
    if (i+1)%4==1:
        name.append(t[i][0:len(t[i])-2])
    elif (i+1)%4==2:
        p=t[i].index(',')
        phone.append(t[i][p+1:len(t[i])-1])
    elif (i+1)%4==3:
        p=t[i].index(',')
        address.append(t[i][p+1:len(t[i])-1])
    elif (i+1)%4==0:
        p=t[i].index(',')
        mail.append(t[i][p+1:len(t[i])-1])
for i in range(len(name)):
    d[name[i]]=[{'phone no':phone[i], 'address':address[i], 'email':mail[i]}]
print("Enter 1 if you want to insert a new entry")
print("Enter 2 if you want to delete an entry")
print("Enter 3 if you want to find all matching entries given a partial name")
print("Enter 4 if you want to find the entry with a phone number or email")
print("Enter 5 if you want to exit")
while True:
    n=int(input("Operation you wish to perform : "))
    if n==1:
        naam=input("Please enter the name")
        no=input("Please enter the phone number")
        pataa=input("Please enter the address")
        em=input("Please enter the email")
        if naam in d.keys():
            q=d[naam]
            q+=[{'phone no':no, 'address':pataa, 'email':em}]
            d[naam]=q
        else:
            d[naam]=[{'phone no':no, 'address':pataa, 'email':em}]
    elif n==2:
        naam=input("Please enter the name")
        no=input("Please enter the phone number")
        pataa=input("Please enter the address")
        em=input("Please enter the email")
        if len(d[naam])==1:
            del d[naam]
        else:
            for i in d[naam]:
                if i['phone no']==no and i['address']==pataa and i['email']==em:
                    i.clear()
    elif n==3:
        pn=input("Please enter name")
        for i in d.keys():
            if pn in i:
                print(i, d[i])
    elif n==4:
        y=input("Please enter the email or phone number")
        for i in d.values():
            for j in i:
                for k in j.values():
                    if k==y:
                        print(list(d.keys())
                              [list(d.values()).index(i)])
                        print(j)
    elif n==5:
        False
        f.close()
        f=open('Addrbook.txt','w')
        for i in fn(d):
            f.writelines(f"{i}:")
            f.writelines('\n')
            for j in d[i]:
                for k in j.keys():
                    f.writelines(f"{k},{j[k]}")
                    f.writelines('\n')
        f.close()
        print(d)
        exit()