for i in range(1000,0,-1):
    c2=i**2
    c=i
    for b in range(1,i+1):
        if (1000-b-c)**2 == c2 - b**2:
            print c,b,(1000-b-c)
            
