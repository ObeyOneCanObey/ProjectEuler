fl=0
n=2000
while fl==0:
    for i in range(1,21):
        if n%i==0:
            fl=1
        else:
            fl=0
    n+=1
    
