def fac(x):
    p=1
    for i in xrange(2,x+1):
        p=p*i
    return p

def com(n,r):
    if n==r:
        return 1
    else:
        return fac(n)/(fac(r)*fac(n-r))

al=0
for n in xrange(1,101):
    for r in xrange(1,n+1):
        if com(n,r)>1000000:
            al+=1

            
    
