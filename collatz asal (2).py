def asalmı(n):
    p=(n**1/2)//1
    if(n==2):
        return(1)
    if(n==((n/2)//1)*2):
        return(0)
    i=3
    while True:
        if(n==((n/i)//1)*i):
            return(0)
        if(i<p):
            i+=2
        else:
            return(1)
alsana[1]
for p in range(2,10000):
    a[1]=1
    c=1
    k=p
    while(k!=1):
       m=1
       if(k%2==0):
            k=k/2
       else:
            k=3*k+1
        m+=1
        c+=1
        if(asalmı(c)==1):
            a.append(c)
print(a)


