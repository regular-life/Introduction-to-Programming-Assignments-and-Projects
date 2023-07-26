n=int(input())
def star(i):
    return('*'*i + '  '*(n-i) + '*'*i)
for i in range(1,n+1) :
    print(star(i))