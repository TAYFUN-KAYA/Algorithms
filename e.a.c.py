def asal(n):
    p=((n**1/2)//1)
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
liste=[]
k=3
a=13195
while(k!=a):
    if(a%k==0):
        if(asal(k)==1):
            liste.append(k)
    print(k)
    k+=2
print(liste)

