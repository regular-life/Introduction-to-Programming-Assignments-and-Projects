def profit(x1,x2):
    if x1>=M and x2>=M:
        return(90*M+100*(x1-M)+25*M+30*(x2-M))
    elif x1>=M and x2<M:
        return(90*M+100*(x1-M)+25*x2)
    elif x1<M and x2>=M:
        return(90*x1+25*M+30*(x2-M))
    else:
        return(90*x1 + 25*x2)
M=int(input("Enter the value of M : "))
arr=[]
p=0
for i in range(1,41):
    for j in range(1,41):
        arr.append(profit(i,j))
        p=max(arr)
        if profit(i,j)==p:
            x1=i
            x2=j
print("No.of Tables is :" , x1)
print("No.of Chairs is :" , x2)
print("Total maximum profit is :" , p)