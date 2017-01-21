l=[1,2,5,10,20,100]
n=0
def como(x,y,z):
    na=1
    n1=0
    n2=z/y
    s=z
    while s==z and n2>0:
        na+=1
        n1+=y
        n2-=x
        s=n1*x+n2*y
    return na


    

    
    
    
