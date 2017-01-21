li=[]
for i in range(0,10):
    n=str(i)
    for j in range(0,10):
        if str(j) in n:
            pass
        else:
            n=n+str(j)
        for k in range(0,10):
            if str(k) in n:
                pass
            else:
                n=n+str(k)
            for l in range(0,10):
                if str(l) in n:
                    pass
                else:
                    n=n+str(l)
                for m in range(0,10):
                    if str(m) in n:
                        pass
                    else:
                        n=n+str(m)
                    for o in range(0,10):
                        if str(o) in n:
                            pass
                        else:
                            n=n+str(o)
                        for p in range(0,10):
                            if str(p) in n:
                                pass
                            else:
                                n=n+str(p)
                            for q in range(0,10):
                                if str(q) in n:
                                    pass
                                else:
                                    n=n+str(q)
                                for r in range(0,10):
                                    if str(r) in n:
                                        pass
                                    else:
                                        n=n+str(r)
                                    li.append(int(n))
                                    print n

                    
            
