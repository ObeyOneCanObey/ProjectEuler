def adi(l1,l2):
    l3=([l1[0]*(l2[1])+l2[0]*(l1[1]),l1[1]*l2[1]])
    return (l3)
        
def div(l):
    return list(l[::-1])

def lk():
    n=0
    a=div(adi([2,1],[1,2]))
    b=div(adi([2,1],a))
    for i in xrange(1,1000):
        a=b
        b=div(adi([2,1],a))
        n1=adi([1,1],b)
        if len(str(n1[0]))>len(str(n1[1])):
            n+=1
    print n

