lepesek = [6500,8200,4300,10100,7600,12000,5400,9800,3900,11200]

ossz=0

for lepes in lepesek:
    ossz+=lepes

atlag=ossz/len(lepesek)    
print(f" 2.feladat: Összesen: {ossz} lépés, átlag: {atlag}")

legt=lepesek[0]
legt_n=1
for i in range(1, len(lepesek)):
    if lepesek[i]>legt:
        legt=lepesek[i]
        legt_n=i+1

print(f"3.feladat: A legtöbb lépés: {legt} a {legt_n}. napon.")        

db=0

for lepes in lepesek:
    if lepes>=10000:
        db+=1
print(f"4.feladat: {db} napon volt legalább 10000 lépés.")        