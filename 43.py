import itertools
pri=[2,3,5,7,11,13,17]
def sust(x):
    x=str(x)
    f=False
    for j in xrange(1,8):
        if int(x[j:j+3])%pri[j-1]==0:
            f=True
        else:
            f=False
            break
    return f

s=0
for i in itertools.permutations('0123456789'):
    z=''
    for k in i:
        z+=k
    if sust(z):
        print z
        s+=int(z)
print '=',s
        
    

    
    
