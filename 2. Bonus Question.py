#Yash Bhardwaj(2022586), Kartikeya(2022241), Aahan Piplani(2022001)
from mediawiki import MediaWiki
import wikiquote
wikipedia=MediaWiki()
s=input("Enter name of the personality : ")
p=wikipedia.page(s)
print("Title :" , p.title)
print("Summary :", p.summary)
n=int(input("How many quotes would you like to print ? "))
p=wikiquote.search(s)
q=wikiquote.quotes(p[0], n)
for i in range(n):
    print(i+1,".", q[i])