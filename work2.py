a=10000 
sum1=10000
for i in range(10):
    a=round(a*(1+0.05),2)
    #print(a)
    if i<3 :
        sum1+=a
print(a,sum1)


