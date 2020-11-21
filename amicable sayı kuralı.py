def d(n):
 toplam=1
 p=2
 q=((n**1/2)//1)
 if(n==((n/p)//1)*p):
     toplam+=p+n/p
 while(p<q):
     p+=1
     if(n==((n/p)//1)*p):
         toplam+=p+n/p
 if(p**2==n):
    toplam-=q
 return(toplam)
gtoplam=0
for n in range(2,10000):
     if(n==d(d(n))):
        gtoplam+=n
        print(gtoplam)
print(gtoplam)
