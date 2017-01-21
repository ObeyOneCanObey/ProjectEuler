def fac(x):
    p=1
    for i in range(1,x+1):
        p=p*i
    return p
print fac(40)/(fac(20)*fac(20))
