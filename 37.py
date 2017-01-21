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


def tru(x):
    m=str(x)
    n=str(m[::-1])
    l=[]
    for i in xrange(len(m)):
        l.append(int(m[i:]))
        l.append(int(n[i:][::-1]))
    f1=False
    for i in l:
        if isprime(i):
            f=True
        else:
            f=False
            break
    return f

n=10
c=0
s=0
while c!=11:
    if isprime(n):
        if tru(n):
            c+=1
            s+=n
            print n
    n+=1
        
        

