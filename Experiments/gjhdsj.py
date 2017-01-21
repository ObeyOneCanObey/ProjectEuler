import math
num=raw_input('::')
mx=0
def pod(x):
    p=1
    n=float(x)/float(10**(len(str(x))))
    for i in range(len(str(x))):
                   no=math.floor(n*10)
                   n=(n*10)-no
                   p=p*no
    return p
l=[]
for i in range(len(num)):
    numo=int(num[i:i+13])
    print numo
    if '0' not in num[i:i+13]:
        ema=pod(numo)
        print 'prod:',ema
        l.append(ema)
        if ema>mx:
            mx=ema
    else:
        print 'Boohoo'
