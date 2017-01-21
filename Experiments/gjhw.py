p=1
for i in xrange(1,101):
    p=p*i
    print p
    print type(p)
p=str(p)
s=0
for i in p:
    s+=int(i)
