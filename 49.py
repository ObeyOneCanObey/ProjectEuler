def prim(x):
    f=False
    for i in range(2,int(float(x)**(0.5))+1):
        if x%i==0:
            f=False
            break
        else:
            f=True
    return f
def perm(x,y):
    f=False
    for i in str(x):
        if i in str(y):
            f=True
        else:
            f=False
            break
    return f

for j in range(1000,3340):
    if prim(j) and prim(j+3330) and prim(j+6660):
        if perm(j,j+3330) and perm(j,j+6660):
            print j,j+3330,+j+6660
    
