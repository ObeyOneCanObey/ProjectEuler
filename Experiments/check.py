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

su=0
for i in xrange(2,2000001):
    if prime(i):
        print i
        su=su+i
print su


