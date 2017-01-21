import itertools
l=[0,1,2,3,4,5,6,7,8,9]
per=itertools.permutations(l)
n=0
for i in per:
    if n==999999:
        print i
        break
    n+=1
