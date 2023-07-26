arr=[]
while True:
    t=tuple(map(str,input().split()))
    if not t:
        False
        arr.sort()
        s=0
        c=0
        for i in range(len(arr)):
            print(arr[i][0],":",arr[i][2])
        for i in range(len(arr)):
            if arr[i][2]=='A+' or arr[i][2]=='A':
                s+=10*int(arr[i][1])
            elif arr[i][2]=='A-':
                s+=9*int(arr[i][1])
            elif arr[i][2]=='B':
                s+=8*int(arr[i][1])
            elif arr[i][2]=='B-':
                s+=7*int(arr[i][1])
            elif arr[i][2]=='C':
                s+=6*int(arr[i][1])
            elif arr[i][2]=='C-':
                s+=5*int(arr[i][1])
            elif arr[i][2]=='D':
                s+=4*int(arr[i][1])
            elif arr[i][2]=='F':
                s+=2*int(arr[i][1])
            c+=int(arr[i][1])
        print("SGPA : ", "%.2f" % (s/c))
    else:
        if t[0][0].isalpha() and t[0][-1].isnumeric():
            if t[1]=='1' or t[1]=='2' or t[1]=='4':
                if t[2]=='A+' or t[2]=='A' or t[2]=='B' or t[2]=='B-' or t[2]=='C' or t[2]=='C-' or t[2]=='D' or t[2]=='F' :
                    arr.append(t)
                else:
                    print("Incorrect Grade")
            else:
                print("Incorrect Credit")
        else:
            print("Improper Course No")