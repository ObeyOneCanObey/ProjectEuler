def fac(x):
    l=[]
    for i in xrange(2,int((600851475143.0**(0.5)))+1):
        if x%i==0:
            l.append(i)
    return l
def prime(x):
    flag=0
    for i in xrange(2,x//2+1):
       if x%i==0:
           flag=1
           break
    if flag==1:
        return False
    else:
        return True

la=[]
for i in fac(600851475143):
    if prime(i):
        la.append(i)
print max(la)
    


