#uzunluğu 500 olan çarpanlarının uzunluğu mesela 6=1+2+3+6=13 olan listeye ekleyip bulma
def bolenler(n):
    carpanlar=[1]
    q=int((n**1/2)//1)
    for p in range(2,q+1):
        if(n%p==0):
            carpanlar.append(p)
            carpanlar.append(int(n/p))
            #extend ile  ekleyebilriiz carpanlar.extend([p,int(n/p)])
    if(q**2==n):
        return(carpanlar[:-1])
    return(carpanlar)
n,sayı=1,1
while(len(bolenler(sayı))<500):
    n+=1
    sayı+=n
print(sayı,n)
#fonksiyonsuz dene
#tele bak orda farklı var orda sadece bölenler sayısını deneyerek yaptık
#hem tel hemde bunu algoritma dene
