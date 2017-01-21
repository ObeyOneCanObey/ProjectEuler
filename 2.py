a=1
b=2
s=2
c=a+b
while c<=4000000:
    if c%2==0 and c<=4000000:
        s+=c
        print s,c
        print 'ya'
    a,b=b,c
    c=a+b


    
