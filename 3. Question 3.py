import random
n=int(input("Input number of files you wish to evaluate "))
z=open("IP Assignment 3\Scores.txt",'w')
z.seek(0,0)
for _ in range(1,n+1):
    f=open(f"IP Assignment 3\File{_}.txt",'r')
    f.seek(0,0)
    t=f.readlines()
    words={}
    for i in range(len(t)):
        t[i]=t[i].lower()
        j=0
        k=''
        while j<(len(t[i])):
            if t[i][j]=='.' or t[i][j]=='!' or t[i][j]==',' or t[i][j]==' ' or t[i][j]=='(' or t[i][j]==')':
                if k in words.keys() and k!='':
                    words[k]+=1
                elif k not in words.keys() and k!='':
                    words[k]=1
                k=''
            else:
                k+=t[i][j]
            j+=1
    words = sorted(words.items(), key=lambda x:x[1])
    total_words=0
    for i in words:
        total_words+=(i[1])
    F1=len(words)/(total_words)
    most_occ=0
    for i in range(1,6):
        most_occ+=words[-i][1]
    F2=most_occ/total_words
    if total_words>750:
        F5=1
    else:
        F5=0
    count=0
    ama=0
    for i in range(len(t)):
        j=0
        while j<len(t[i]):
            if (t[i][j]=='.' or t[i][j]==',' or t[i][j]==';' or t[i][j]==':'):
                if last_ch=='.' or last_ch==',' or last_ch==';' or last_ch==':':
                    pass
                    ama=+1
                else:
                    if ama==2:
                        count+=1
                    last_ch=t[i][j]
            else:
                last_ch=t[i][j]
                ama=0
            j+=1
    F4=count/total_words
    sentences=[]
    k=''
    for i in t:
        j=0
        while j<len(i):                
            if i[j]=='.' or i[j]=='!':
                sentences.append(k)
                k=''
            else:
                k+=i[j]
            j+=1
    cnt=0
    for i in sentences:
        if i.count(' ')>34 or i.count(' ')<4:
            cnt+=1
    F3=cnt/len(sentences)
    score=4 + F1*6 + F2*6 -F3 - F4 - F5
    z.write(f"File{_}.txt")
    z.write('\n')
    z.write(f"score : {score} ")
    z.write('\n')
    k=''
    for i in range(1,6):
        k+=(words[-i][0])
        if i!=5:
            k+=', '
    z.write(f"most frequently occuring words in descending order are : {k}")
    z.write('\n')
    natnos=[i for i in range(len(words))]
    k=''
    for i in range(5):
        ni=random.randint(0,len(natnos)-1)
        no=natnos[ni]
        k+=words[no][0]
        if i!=4:
            k+=', '
    z.write(f"randomly selected words : {k}")
    # print(F1,F2,F3,F4,F5)
z.close()