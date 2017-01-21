l=[]
for i in xrange(2,101):
    for j in xrange(2,101):
        if i**j not in l:
            l.append(i**j)
print len(l)
