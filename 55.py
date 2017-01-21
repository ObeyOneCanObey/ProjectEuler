n=0
n1=0
for i in xrange(10,10001):
    a=0
    b=True
    st=str(i)
    while a<50:
        a+=1
        st=str(int(st)+int(st[::-1]))
        if st==st[::-1]:
            n+=1
            b=False
            break
    if b:
        print i
        n1+=1
        
print n,n1
print 10000-n

        
        
        
        
