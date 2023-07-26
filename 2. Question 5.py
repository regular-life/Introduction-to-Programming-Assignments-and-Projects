ax=[]
ay=[]
while True:
    try:
        x,y=map(int,input().split(','))
        ax.append(x)
        ay.append(y)
    except ValueError:
        cx=int(input())
        cy=int(input())
        for i in range(len(ax)):
            ax[i]*=cx
            ay[i]*=cy
        for x,y in zip(ax,ay):
            print(x,",",y)
        False
        break