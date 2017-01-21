def fac(x):
    l=[1]
    for i in xrange(2,int(float(x)**(0.5))+1):
        if x%i==0:
            l.append(i)
            l.append(x/i)
    return list(set(l))


def abun(x):
    if x==4:
        return False
    if sum(fac(x))>x:
        return True
    else:
        return False


alnum=[]
allabun=[]

s=0
for k in xrange(1,28124):
    s+=k
    if abun(k):
        allabun.append(k)

print s



for i in range(len(allabun)):
    for j in range(i,len(allabun)):
        if allabun[i]+allabun[j]<=28123:
            alnum.append(allabun[i]+allabun[j])

sa=sum(list(set(alnum)))

           

print s-sa


