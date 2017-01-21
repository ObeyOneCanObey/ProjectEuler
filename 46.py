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

sq=[]
lx=[]
n=9
m=1
while 1==1:
    for i in xrange(m,n):
        sq.append(2*(i**2))
    if not pri(n):
        lx.append(n)
        for j in sq:
            if j<n:
                if pri(n-j):
                    try:
                        lx.remove(n)
                    except:
                        pass
    if len(lx)>0:
        print lx
                    
                    

    m=n
    n+=2
        
        
