def pand(x,y):
    z=str(x)+str(y)+str(x*y)
    f=False
    if len(z)!=9 and '0' in z:
        f=False
    else:
        for i in xrange(1,10):
            if len(z.split(str(i)))==2:
                f=True
            else:
                f=False
                break
    return f

l=[]
for i in xrange(1,2000):
    for j in xrange(1,2000):
        if pand(i,j) and j*i not in l:
            l.append(i*j)
            print str(i)+str(j)+str(i*j)

print sum(l)


