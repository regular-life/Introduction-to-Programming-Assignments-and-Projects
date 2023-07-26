import random
import requests
arr=["above","alive","alone","angry","aware","awful","brave","brief","broad","cheap","chief","civil","clean","dirty","daily","early","empty","equal","extra","final","first","fresh","front","funny","giant","happy","harsh","ideal","joint","large","legal","light","lucky","magic","moral","nasty","naked","naval","other","quick","proud","quick","rapid","rough","round","royal","silly","smart","solid","sorry"]
a=random.randint(0,49)
word=arr[a]
q=''
c=0
while q!=word and c<6:
    q=''
    print("You have {} turns left.".format(6-c))
    s=input("Guess the word : ")
    req=requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(s))
    req=req.text
    if "No Definitions Found" in req:
        print("Please type a valid word.")
    else:
        c+=1
        for i,j in zip(s,word):
            if i==j:
                q+=i
            else:
                q+='-'
        print(q)
        if q.count('-')>0:
            lst=[]
            for i in s:
                if i in word and i not in q:
                    lst.append(i)
            lst=set(lst)
            print("Other characters present : ", *lst)
        else:
            print("Congratulations ! You guessed it right ! The answer is {}".format(q))