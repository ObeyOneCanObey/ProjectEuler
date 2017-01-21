def pen(x):
    return (3*x-1)*x/2

def chp(x):
    x=abs(x)
    l=(((2.0*x/3.0)+1.0/36.0)**(0.5)+1.0/6.0)
    if float(int(float(int(((2.0*x/3.0)+1.0/36.0)**(0.5)+1.0/6.0))))==l:
        return True
    else:
        return False

print chp(pen(4)+pen(7))


for i in xrange(1,200000):
    for j in xrange(i+1,200000):
        if chp(abs(pen(i)-pen(j))) and chp(abs(pen(i)+pen(j))):
            print abs(i-j)



'''n=2

mi=1000000

while 1==1:
    a=pen(n)
    m=n+1
    b=pen(m)
    while not chp(a+b):
        m+=1
        b=pen(m)
        if chp(a-b):
            print abs(a+b)
    n+=1'''
