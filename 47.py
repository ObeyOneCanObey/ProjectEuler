def pri(n):
    f=False
    if n==2 or n==3:
        f=True
    else:
        for i in range(2,int(float(n)**(0.5))+1):
            if n%i==0:
                f=False
                break
            else:
                f=True
    return f
    

def num(n):
    l=[]
    for i in range(2,int(float(n)**(0.5))+1):
        if pri(i):
            if n%i==0:
                l.append(i)
        if pri(n/i):
            if n%(n/i)==0:
                l.append(n/i)
    return len(list(set(l)))

print num(644),num(645),num(646)


la=[0,0,0,0]
n=4
while 1==1:
    la.append(num(n))
    if la[n]==4 and la[n-1]==4 and la[n-2]==4 and la[n-3]==4:
        print n-3
        break
    n+=1
    
    










