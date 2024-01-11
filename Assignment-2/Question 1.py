items=["Samosa", "Idli", "Maggie", "Dosa", "Tea", "Coffee", "Sandwich", "ColdDrink"]
price=[15,30,50,70,10,20,35,35]
for i in range(len(items)):
    print((i+1), items[i], price[i])
arr=[]
c=0
t=0
for i in range(len(items)):
    arr.append(0)
while True:
    try:
        i,n=map(int,input().split())
        arr[i-1]+=n
        c+=n*price[i-1]
        t+=n
    except ValueError:
        False
        for i in range(len(items)):
            if arr[i]>0:
                print(items[i],",", arr[i],",",  "Rs", price[i]*arr[i])
        print('\n')
        print("TOTAL",",",  t, "items",",",  "Rs", c)