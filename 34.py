def fac(x):
    p=1
    for i in xrange(2,x+1):
        p=p*i
    return p

def sufac(x):
    s=0
    for i in str(x):
        s+=fac(int(i))
    return s

n=3
su=0
while 1==1:
    if n==sufac(n):
        su+=n
        print su
    n+=1
    
