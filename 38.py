def pand(z):
    f=False
    if len(z)!=9 and '0' in z:
        f=False
    else:
        for i in xrange(1,10):
            if len(z.split(str(i)))==2:
                f=True
            else:
                f=False
                break
    return f

ma=0
for i in xrange(1,10000):
    n=1
    z=''
    while len(z)<=6:
        z+=str(i*n)
        n+=1
    if pand(z):
        print z
        if ma<int(z):
            ma=z
print ma
            
    
    
    
    
