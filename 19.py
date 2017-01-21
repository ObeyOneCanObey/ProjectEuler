day=['m','t','w','th','f','s','su']

mon1=[31,28,31,30,31,30,31,31,30,31,30,31]
mon2=[31,29,31,30,31,30,31,31,30,31,30,31]

def moth(x):
    for i in xrange(x):
        du=day[0]
        if i+1==1 and du=='m':
            print 'yes'
        del day[0]
        day.append(du)

    

nu=0
for i in xrange(1900,2001):
    if i%100==0:
        if i%400==0:
            for j in mon2:
                moth(j)
    elif i%4==0:
        for j in mon2:
            moth(j)
    else:
        for j in mon1:
            moth(j)
        
    
