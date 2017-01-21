'''n=0
m=1
co=0
#while 1==1:
    #for i in xrange(10**n,10**m):
        #if float(i)**(float(1.0/len(str(i)))).is_integer():
            #print i
    #n+=1
    #m+=1
float(16807)**(float(1.0/len(str(16807)))).is_integer()  '''

def na(n):
    p=1
    nu=n**p
    while len(str(nu))<=p:
        print nu
        p+=1
        nu=n**p
        if len(str(nu))==p:
            print nu
            
