n=int(input("Insert number here : "))
s=str(n)
l=len(s)
d1=["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine"]
d2=["Eleven" , "Twelve" , "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" , "Eighteen" , "Nineteen" , "Twenty"]
d3=["Ten" , "Twenty", "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
d4=["Hundred" , "Thousand" , "Lakh" , "Crore"]
if l==1:
    if n==0:
        print("Zero")
    else:
        print(d1[n])
elif l==2:
    if int(s[-2])==1:
        if n==10:
            print(d3[0])
        else:
            print(d2[n-11])
    else:
        print(d3[n//10 -1] , d1[n%10])
elif l==3:
    print(d1[int(s[0])] , d4[0] , end=" ")
    n=int(n%100)
    s=str(n)
    l=len(s)
    if l==1:
        print(d1[n])
    elif l==2:
        if int(s[-2])==1:
            if n==10:
                print(d3[0])
            else:
                print(d2[n-11])
        else:
            print(d3[n//10 -1] , d1[n%10])
elif l==4:
    print(d1[int(s[0])] , d4[1] , end=" ")
    n=int(n%1000)
    s=str(n)
    l=len(s)
    if l==1:
        print(d1[n])
    elif l==2:
        if int(s[-2])==1:
            if n==10:
                print(d3[0])
            else:
                print(d2[n-11])
        else:
            print(d3[n//10 -1] , d1[n%10])
    elif l==3:
        print(d1[int(s[0])] , d4[0] , end=" ")
        n=int(n%100)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
elif l==5:
    k=n//1000
    r=str(k)
    if int(r[-2])==1:
        if k==10:
            print(d3[0], end=" ")
        else:
            print(d2[k-11] , end=" ")
    else:
        print(d3[k//10 -1] , d1[k%10] , end=" ")
    print(d4[1] , end=" ")
    n=int(n%1000)
    s=str(n)
    l=len(s)
    if l==1:
        print(d1[n])
    elif l==2:
        if int(s[-2])==1:
            if n==10:
                print(d3[0])
            else:
                print(d2[n-11])
        else:
            print(d3[n//10 -1] , d1[n%10])
    elif l==3:
        print(d1[int(s[0])] , d4[0] , end=" ")
        n=int(n%100)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
elif l==6:
    print(d1[int(s[0])] , d4[2] , end=" ")
    n=int(n%100000)
    s=str(n)
    l=len(s)
    k=n//10000
    if l==1:
        print(d1[n])
    elif l==2:
        if int(s[-2])==1:
            if n==10:
                print(d3[0])
            else:
                print(d2[n-11])
        else:
            print(d3[n//10 -1] , d1[n%10])
    elif l==3:
        print(d1[int(s[0])] , d4[0] , end=" ")
        n=int(n%100)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
    elif l==4:
        print(d1[int(s[0])] , d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
    elif l==5:
        k=n//1000
        r=str(k)
        if int(r[-2])==1:
            if k==10:
                print(d3[0], end=" ")
            else:
                print(d2[k-11] , end=" ")
        else:
            print(d3[k//10 -1] , d1[k%10] , end=" ")
        print(d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
elif l==7:
    k=n//100000
    r=str(k)
    if int(r[-2])==1:
        if k==10:
            print(d3[0], end=" ")
        else:
            print(d2[k-11] , end=" ")
    else:
        print(d3[k//10 -1] , d1[k%10] , end=" ")
    print(d4[2] , end=" ")
    n=int(n%100000)
    s=str(n)
    l=len(s)
    if l==1:
        print(d1[n])
    elif l==2:
        if int(s[-2])==1:
            if n==10:
                print(d3[0])
            else:
                print(d2[n-11])
        else:
            print(d3[n//10 -1] , d1[n%10])
    elif l==3:
        print(d1[int(s[0])] , d4[0] , end=" ")
        n=int(n%100)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
    elif l==4:
        print(d1[int(s[0])] , d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
    elif l==5:
        k=n//1000
        r=str(k)
        if int(r[-2])==1:
            if k==10:
                print(d3[0], end=" ")
            else:
                print(d2[k-11] , end=" ")
        else:
            print(d3[k//10 -1] , d1[k%10] , end=" ")
        print(d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
elif l==8:
    print(d1[int(s[0])] , d4[3] , end=" ")
    n=int(n%10000000)
    s=str(n)
    l=len(s)
    k=n//1000000
    if l==1:
        print(d1[n])
    elif l==2:
        if int(s[-2])==1:
            if n==10:
                print(d3[0])
            else:
                print(d2[n-11])
        else:
            print(d3[n//10 -1] , d1[n%10])
    elif l==3:
        print(d1[int(s[0])] , d4[0] , end=" ")
        n=int(n%100)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
    elif l==4:
        print(d1[int(s[0])] , d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
    elif l==5:
        k=n//1000
        r=str(k)
        if int(r[-2])==1:
            if k==10:
                print(d3[0], end=" ")
            else:
                print(d2[k-11] , end=" ")
        else:
            print(d3[k//10 -1] , d1[k%10] , end=" ")
        print(d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
    elif l==6:
        print(d1[int(s[0])] , d4[2] , end=" ")
        n=int(n%100000)
        s=str(n)
        l=len(s)
        k=n//10000
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
        elif l==4:
            print(d1[int(s[0])] , d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])
        elif l==5:
            k=n//1000
            r=str(k)
            if int(r[-2])==1:
                if k==10:
                    print(d3[0], end=" ")
                else:
                    print(d2[k-11] , end=" ")
            else:
                print(d3[k//10 -1] , d1[k%10] , end=" ")
            print(d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])
    elif l==7:
        k=n//100000
        r=str(k)
        if int(r[-2])==1:
            if k==10:
                print(d3[0], end=" ")
            else:
                print(d2[k-11] , end=" ")
        else:
            print(d3[k//10 -1] , d1[k%10] , end=" ")
        print(d4[2] , end=" ")
        n=int(n%100000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
        elif l==4:
            print(d1[int(s[0])] , d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])
        elif l==5:
            k=n//1000
            r=str(k)
            if int(r[-2])==1:
                if k==10:
                    print(d3[0], end=" ")
                else:
                    print(d2[k-11] , end=" ")
            else:
                print(d3[k//10 -1] , d1[k%10] , end=" ")
            print(d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])
elif l==9:
    k=n//10000000
    r=str(k)
    if int(r[-2])==1:
        if k==10:
            print(d3[0], end=" ")
        else:
            print(d2[k-11] , end=" ")
    else:
        print(d3[k//10 -1] , d1[k%10] , end=" ")
    print(d4[3] , end=" ")
    n=int(n%10000000)
    s=str(n)
    l=len(s)
    if l==1:
     print(d1[n])
    elif l==2:
        if int(s[-2])==1:
            if n==10:
                print(d3[0])
            else:
                print(d2[n-11])
        else:
            print(d3[n//10 -1] , d1[n%10])
    elif l==3:
        print(d1[int(s[0])] , d4[0] , end=" ")
        n=int(n%100)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
    elif l==4:
        print(d1[int(s[0])] , d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
    elif l==5:
        k=n//1000
        r=str(k)
        if int(r[-2])==1:
            if k==10:
                print(d3[0], end=" ")
            else:
                print(d2[k-11] , end=" ")
        else:
            print(d3[k//10 -1] , d1[k%10] , end=" ")
        print(d4[1] , end=" ")
        n=int(n%1000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
    elif l==6:
        print(d1[int(s[0])] , d4[2] , end=" ")
        n=int(n%100000)
        s=str(n)
        l=len(s)
        k=n//10000
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
        elif l==4:
            print(d1[int(s[0])] , d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])
        elif l==5:
            k=n//1000
            r=str(k)
            if int(r[-2])==1:
                if k==10:
                    print(d3[0], end=" ")
                else:
                    print(d2[k-11] , end=" ")
            else:
                print(d3[k//10 -1] , d1[k%10] , end=" ")
            print(d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])
    elif l==7:
        k=n//100000
        r=str(k)
        if int(r[-2])==1:
            if k==10:
                print(d3[0], end=" ")
            else:
                print(d2[k-11] , end=" ")
        else:
            print(d3[k//10 -1] , d1[k%10] , end=" ")
        print(d4[2] , end=" ")
        n=int(n%100000)
        s=str(n)
        l=len(s)
        if l==1:
            print(d1[n])
        elif l==2:
            if int(s[-2])==1:
                if n==10:
                    print(d3[0])
                else:
                    print(d2[n-11])
            else:
                print(d3[n//10 -1] , d1[n%10])
        elif l==3:
            print(d1[int(s[0])] , d4[0] , end=" ")
            n=int(n%100)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
        elif l==4:
            print(d1[int(s[0])] , d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])
        elif l==5:
            k=n//1000
            r=str(k)
            if int(r[-2])==1:
                if k==10:
                    print(d3[0], end=" ")
                else:
                    print(d2[k-11] , end=" ")
            else:
                print(d3[k//10 -1] , d1[k%10] , end=" ")
            print(d4[1] , end=" ")
            n=int(n%1000)
            s=str(n)
            l=len(s)
            if l==1:
                print(d1[n])
            elif l==2:
                if int(s[-2])==1:
                    if n==10:
                        print(d3[0])
                    else:
                        print(d2[n-11])
                else:
                    print(d3[n//10 -1] , d1[n%10])
            elif l==3:
                print(d1[int(s[0])] , d4[0] , end=" ")
                n=int(n%100)
                s=str(n)
                l=len(s)
                if l==1:
                    print(d1[n])
                elif l==2:
                    if int(s[-2])==1:
                        if n==10:
                            print(d3[0])
                        else:
                            print(d2[n-11])
                    else:
                        print(d3[n//10 -1] , d1[n%10])