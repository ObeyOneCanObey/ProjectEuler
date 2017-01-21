def isprime(x):
    f=False
    for i in xrange(2,int(float(x)**(0.5))+1):
        if x%i==0:
            f=False
            break
        else:
            f=True
    if x==2 or x==3:
        f=True
    return f


def cir(x):
    m=str(x)
    l=[]
    n=0
    for i in m:
        l.append(int(m[n:]))
        m=m+i
        n+=1
    f1=False
    for i in l:
        if isprime(i):
            f=True
        else:
            f=False
            break
    return f

n=0
for i in xrange(2,1000000):
    if isprime(i):
        if cir(i):
            n+=1
            
    


    
