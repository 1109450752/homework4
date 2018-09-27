for i in range(1,10000):
    q=1
    sum1=0
    while q<=i:
        if i%q==0:
            sum1=sum1+q
            #print(q," :",end="")
        q+=1
    #print(sum1-i,i)
    sum1=sum1-i
    #print()
    if sum1==i:
        print(sum1)
