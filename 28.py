m=[]
l=[]
for i in xrange(1001):
    l.append(0)
for j in xrange(1001):
    m.append(list(l))
def halla():
    for i in m:
        print i
sign=1
num=1
row=500
col=500
m[row][col]=num

for i in xrange(1,1002):
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

su=-1
for i in xrange(len(m)):
    su=su+m[i][i]+m[i][1000-i]
    #print m[i][i],m[i][1000-i],
    

        
    
    
    
    
    
    
    

    
