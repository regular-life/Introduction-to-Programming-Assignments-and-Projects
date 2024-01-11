n=int(input())
def stars(n,i):
    if i==n-1:
        return(stars2(n,n-1))
    print('* '*(n-i)+' '*4*i+'* '*(n-i))
    return(stars(n,i+1))
def stars2(n,i):
    if i==-1:
        return
    print('* '*(n-i)+' '*4*i+'* '*(n-i))
    return(stars2(n,i-1))
stars(n,0)