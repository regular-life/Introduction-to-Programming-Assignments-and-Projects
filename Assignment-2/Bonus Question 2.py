#Yash Bhardwaj(2022586), Kartikeya(2022241), Aahan Piplani(2022001)
import requests 
import urllib.request
import json
from PIL import Image
s = input("Enter the word to get summary from wikipedia : ")
try:
    i=s.index(' ')
    k=list(s)
    if k[0].islower():
        k[0]=chr(ord(s[0])-32)
    if k[i+1].islower():
        k[i+1]=chr(ord(s[i+1])-32)
    s=''
    for i in k:
        s+=i
except ValueError:
    k=list(s)
    if k[0].islower():
        k[0]=chr(ord(s[0])-32)
    s=''
    for i in k:
        s+=i
print(s)
response1 = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{s}")
t=response1.json()
summary=t['extract']
print(summary)
if input("Would you like to see the image from the said article ? ").lower()=='yes':
    s=t['title']
    response2 = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&titles={s}&pithumbsize=500")
    data2 = response2.json()
    page_id = list(data2["query"]["pages"].keys())[0]
    if page_id != '-1':
        im=urllib.request.urlretrieve(data2["query"]["pages"][page_id]["thumbnail"]["source"],"image.png")
        im=Image.open("image.png")
        im.show()
    else:
        print("Sorry ! No photograph found!")