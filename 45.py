def tri(x):
    l=((2.0*x)+0.25)**(0.5)-0.5
    if float(int(((2.0*x)+0.25)**(0.5)-0.5))==l:
        return True
    else:
        return False

def pen(x):
    l=(((2.0*x/3.0)+1.0/36.0)**(0.5)+1.0/6.0)
    if float(int(float(int(((2.0*x/3.0)+1.0/36.0)**(0.5)+1.0/6.0))))==l:
        return True
    else:
        return False

def heg(x):
    l=(x/2.0+1.0/16.0)**(0.5)+0.25
    if float(int((x/2.0+1.0/16.0)**(0.5)+0.25))==l:
        return True
    else:
        return False
    
n=243.0
while 1==1:
    f=n*(n+1.0)/2.0
    if pen(f) and heg(f):
        print f
    n+=1.0





        
        
        
    
                
                    
            
    
