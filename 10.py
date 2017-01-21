def prime(x):
    flag=0
    for i in xrange(2,int(float(x)**0.5)+1):
       if x%i==0:
           flag=1
           break
    if flag==1:
        return False
    else:
        return True

s=0
for i in xrange(2,2000001):
    if prime(i):
        s+=i

