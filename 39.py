def co(x):
    n=0
    for i in range(x,0,-1):
        c2=i**2
        c=i
        for b in range(1,i+1):
            a=(x-b-c)
            if a**2 == c2 - b**2 and b>0 and c>0 and a>0 and b>a:
                n+=1
    return n


ma=0
for i in xrange(1000):
    if ma<co(i) and co(i)>0:
        ma=co(i)
        print i

    
            
