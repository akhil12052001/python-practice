val=int(input("enter a value"))
for i in range(2,val):
    count=0
    if(val%i==0):
        count=1
        if(count==1):
            print("prime",val)
        else:
            print("non prime",val)

                            