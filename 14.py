
l=[0,1,2]

def collatz(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
    
'''m=0
for i in xrange(1,1000001):
    l=[i]
    f=0
    while f==0:
        if l[-1]%2==0:
            l.append(l[-1]/2)
        else:
            l.append(l[-1]*3 + 1)
        if l[-1]==1:
            if len(l)>m:
                m=len(l)
            f=1'''
for i in xrange(3,1000001):
    l.append(0)
    la=2
    a=collatz(i)
    while a!=1:
        if collatz(a)<len(l):
            la+=l[collatz(a)]
            a=1
        else:
            a=collatz(a)
            la+=1
    l[i]=la
print max(l)

    
        
    
    


    
