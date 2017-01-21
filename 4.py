l=[]
for i in xrange(100,1000):
    for j in xrange(i,1000):
        nu=str(i*j)
        if nu==nu[::-1]:
            l.append(int(nu))
            
        
