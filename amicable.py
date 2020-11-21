#karşılıklı iki sayı bölenlerinin eşit olması
n=int(input("sayı giriniz :"))
toplam=1
q=int((n**1/2)//1)
for p in range(2,q+1):
    if(n%p==0):
        toplam+=p+n/p
if(q**2==n):
    toplam=toplam-q
print(int(toplam))

    #fonksiyon ile 10000 den küçük birbirine çarpanları eşit olan 
def d(n):
    toplam=1
 q=int((n**1/2)//1)
 for p in range(2,q+1):
    if(n%p==0):
        toplam+=p+n/p
 if(q**2==n):
    toplam=toplam-q
 retrun(toplam)
gtoplam=0
for m in range(2,10000):
    s=d(m)
    if(m==s):
        continue
    if(s>10000):
               #burada 10000 den büyükleri istemiyoruz
            continue
    if(m==d(s)):
        gtoplam+=m
print(gtoplam)