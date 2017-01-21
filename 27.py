def isprime(x):
    f=False
    for i in xrange(2,int(float(x)**(0.5))+1):
        if x%i==0:
            f=False
            break
        else:
            f=True
    return f
bl=[]

for i in xrange(2,1000):
    if isprime(i):
        bl.append(i)
        bl.append(i*(-1))
l=[]

def ex(a,b,n):
    return (n**2)+(a*n)+b

for a in xrange(-999,1000):
    for b in bl:
        n=0
        while isprime(abs(ex(a,b,n))):
            n+=1
        l.append([n,a*b])
print 'yes'


for i in l:
    if i[0]==71:
        print i[1]

