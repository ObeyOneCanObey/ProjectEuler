a=1
b=1
n=2
while True:
    n+=1
    c=a+b
    if len(str(c))==1000:
        print n
        break
    a,b=b,c
        
