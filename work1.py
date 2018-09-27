i=0
i1=0
sum1=0
a=eval(input(">>"))
while a!=0:
    a=eval(input(">>"))
    if a<0:
        i+=1
    else :
        i1+=1
    sum1=sum1+a
print("zheng{} fu{} pingjun{}".format(i,i1,sum1/(i+i1)))

