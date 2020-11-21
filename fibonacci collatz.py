#hem collatz hemde fibonacci
fib1=1
fib2=1
col=[1]
for p in range(2,1000000):
  n=p
  c=1
  while(n!=1):    
    fib=fib1+fib2
    fib1=fib2
    fib2=fib
    if(n%2==0):
      n=n/2
    else:  
      n=3*n+1
    if(n<p):
        c=c+col[n]
        col.append(c)
        break 
    c+=1
    if(fib==c):
      print(fib)
      continue      
       