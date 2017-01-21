def pr(x):
    f=False
    if x==2 or x==3:
        f=True
    elif x==1:
        f=False
    else:
        for i in xrange(2,int(float(x)**(0.5))+1):
            if x%i==0:
                f=False
                break
            else:
                f=True
    return f

m=[]
l=[]
for i in xrange(20001):
    l.append(0)
for j in xrange(20001):
    m.append(list(l))
def halla():
    for i in m:
        print i
sign=1
num=1
row=10000
col=10000
m[row][col]=num

for i in xrange(1,20002):
    try:
        for j in xrange(i):
            col+=sign
            num+=1
            m[row][col]=num
        for k in xrange(i):
            row+=sign
            num+=1
            m[row][col]=num
        sign=sign*(-1)
    except:
        print num

ll=[]
lr=[]
for i in xrange(len(m)):
    ll.append(m[i][i])
    lr.append(m[i][20000-i])


el=[]
n=3
np=0
for i in xrange(1,10001):
    el1=[ll[10000+i],ll[10000-i],lr[10000+i],lr[10000-i]]
    nel=n*2-1
    for i in el1:
        if pr(i):
            np+=1
    if float(np)*100.0/float(nel)<10.0:
        print n,float(np)*100.0/float(nel)
    n+=2




