def asalmı(n):
    q=((n**1/2)//1)
    if(n==2):
        return(0)
    if(n%2==0):
        return(0)
    p=3
    while True:
         if((n==((n/p)//1)*p) and n!=p):
             return(0)
         if(p<q):
             p+=2
         else:
             return(1)
print(asalmı(8))