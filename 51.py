def perm(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = list(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield list(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield list(pool[i] for i in indices[:r])
                break
        else:
            return

def pri(x):
    f=False
    if x==2 or x==3:
        f=True
    else:
        for i in xrange(2,int(float(x)**(0.5))+1):
            if x%i==0:
                f=False
                break
            else:
                f=True
    return f
    

def prl(y):
    ln=[]
    for i in xrange(10):
        lo=[]
        for i in perm(str(y)+str(i)+str(i)):
            
    
    



n=2
m=3
f=True
while f:
    for i in xrange(10**n,10**m+1):
        #function



    m+=1
    n+=1

