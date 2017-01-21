from math import floor
num=raw_input('::')
mx=0
def pod(x):
    su=1
    for i in range(len(str(x))):
        p=((x/(10**(len(str(x))-i)).floor())
        su=su*p
    return su
for i in range(len(num)):
    numo=int(num[i:i+13])
    print numo
    ema=pod(numo)
    print ema
    if ema>mx:
        mx=ema

