def prim(x):
    f=False
    if x==3 or x==2:
        f=True
    else:
        for i in xrange(2,int(float(x)**(0.5))+1):
            if x%i==0:
                f=False
                break
            else:
                f=True
    return f


s=0
i=0
while s<1000000:
    if prim(i):
        s+=i
        print i
        if prim(s) and s<1000000:
            print s
    i+=1
    
            
