m=0
for i in xrange(1,100):
    for j in xrange(1,100):
        s=str(i**j)
        su=0
        for k in s:
            su+=int(k)
        if su>m:
            m=su

            
