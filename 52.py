def checa(x,y):
    f1=False
    f2=False
    for i in str(x):
        if i in str(y):
            f1=True
        else:
            f1=False
            break
    for i in str(y):
        if i in str(x):
            f2=True
        else:
            f2=False
            break
    
    return f1 and f2
    



def bugga(x):
    f=True
    la=[str(x),str(2*x),str(3*x),str(4*x),str(5*x),str(6*x)]
    for k in xrange(len(la)):
        for j in xrange(k+1,len(la)):
            if checa(la[k],la[j]):
                f=f and True
            else:
                f=f and False
                break
    return f
            


t=True
a=1
b=2
while t:
    for l in xrange(10**a,10**b//6+3):
        if bugga(l):
            print l
            t=False
            break
        
    a+=1
    b+=1


