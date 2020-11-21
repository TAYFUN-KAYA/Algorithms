pmax=0
cmax=0
col=[1]
for p in range(2,1000000):
    n=p
    c=1
    while(n!=1):
        if(n%2==0):
            n=n/2
            int(n)
        else:
            n=3*n+1
        if(n<p):
            c=c+col[int(n)]
            col.append(c) 
            break
        print(col)
        c+=1
    if(c>cmax):
            cmax=c
            pmax=p
print(pmax)



