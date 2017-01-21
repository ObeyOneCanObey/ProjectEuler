def div(n):
    l=[]
    for i in xrange(1,n//2+1):
        if n%i==0:
            l.append(i)
    return sum(l)
la=[]
for i in xrange(2,10000):
    na=div(i)
    if na!=1 and na<10000:
        la.append([i,div(i)])
am=[]
for i in la:
    if i[::-1] in la:
        am.append(i)
        la.remove(i)


        
    
