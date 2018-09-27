import math
q=0
n=10000
i=1
j=0
for i1 in range(10):
    while i<=n*2-1:
        q=q+(1/i)*math.pow(-1,j)
        i+=2
        j+=1
    print(q*4)
    n=n+10000
