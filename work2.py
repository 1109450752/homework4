a=10000 
sum1=0
for i in range(10):
    a=round(a*(1+0.05),2)
print(a)
for i in range(4):
   sum1 = sum1 + a
   a=round(a*(1+0.05),2)
   print(sum1)


