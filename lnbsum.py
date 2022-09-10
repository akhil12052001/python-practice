sum=0
lst=[]
for i in range(5):

    
    a=int(input())
    lst.append(a)
    if(a<9):
     lst.remove(a)
    else:
       sum=sum+a

print("the sum is:{}".format(sum))

print("values are:{}".format(lst))


