

'''def pri(n):
    f=False
    if n==2 or n==3:
        f=True
    else:
        for i in range(2,int(float(n)**(0.5))+1):
            if n%i==0:
                f=False
                break
            else:
                f=True
    return f
    
def div(n):
    p=1
    z=int(n)
    for i in xrange(2,n):
        if pri(i):
            o=0
            while z%i==0:
                o+=1
                z=z/i
            p=p*o
    return p'''


    
def fac(n):
    l=[]
    for i in xrange(2,int(float(n)**(0.5))+1):
        if n%i==0:
            l.append(i)
            l.append(n/i)
    return len(list(set(l)))+2
        
        
ni=7
while 1==1:
    if fac(ni*(ni+1)/2)>500:
        print ni*(ni+1)/2
        break
    ni+=1


    
