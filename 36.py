s=0
for i in xrange(1,1000000):
    st=bin(i)[2:]
    if str(i)==str(i)[::-1] and st==st[::-1]:
        s+=i
