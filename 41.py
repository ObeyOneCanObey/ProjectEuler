import itertools


def prim(x):
    f=False
    for i in xrange(2,int(float(x)**(0.5))+1):
        if x%i==0:
            f=False
            break
        else:
            f=True
    return f

ma=0
for k in xrange(9,2,-1):
    s=''
    for j in xrange(1,k+1):
        s+=str(j)
    for m in itertools.permutations(s):
        nu=''
        for n in m:
            nu+=n
        if prim(int(nu)):
            if int(nu)>ma:
                ma=int(nu)
print ma
    
    
