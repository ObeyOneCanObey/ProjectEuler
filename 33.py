def com(x,y):
    lx=[]
    ly=[]
    for i in str(x):
        lx.append(i)
    for i in str(y):
        if i in lx:
            lx.remove(i)
        else:
            ly.append(i)
    if len(lx)!=1 or float(x)%10.0==0:
        return 1
    else:
        return float(lx[0])/float(ly[0])

p=1
for i in xrange(10,100):
    for j in xrange(i+1,100):
        try:
            ev1=float(i)/float(j)
            ev2=com(str(i),str(j))
            if ev1==ev2:
                print i,j
        except:
            pass
print p
        
        

        
    
    
