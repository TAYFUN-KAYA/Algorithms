def asal(n):
    p=(n**1/2)//1
    if(n==2):
        return(1)
    if(n%2==0):
        return(0)
    i=3
    while True:
        if(n%i==0 and i!=n):
            return(0)
        if(i<p):
            i+=2
        else:
            return(1)
toplam=0
for a in range(2,1000001):
    if(asal(a)==1):
        toplam+=a
        print(toplam)
    print(a)
print(toplam)

