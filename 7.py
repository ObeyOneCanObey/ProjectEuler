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

l=[]
n=2
while len(l)!=10001:
    if prime(n):
        l.append(n)
    n+=1
    
