ones=[0,3,3,5,4,4,3,5,5,4]
teno=[3,6,6,8,8,7,7,9,8,8]
tens=[0,3,6,6,5,5,5,7,6,6]

s=0

for i in range(320,321):
    num=str(i)
    if len(num)==1:
        s+=ones[int(num[0])]
    elif len(num)==2:
        if num[0]==1:
            s+=teno[int(num[1])]
        else:
            s=s+tens[int(num[0])]+ones[int(num[1])]
    elif len(num)==3:
        if num[1]==1:
            s=s+ones[int(num[0])]+10+teno[int(num[1])]
        else:
            s=s+tens[int(num[1])]+ones[int(num[0])]+ones[int(num[2])]+10
        if int(num)%100==0:
            s=s-3
            print num
    elif len(num)==4:
        s+=11
        print num,'yaya'
print s


        
        
            
        
