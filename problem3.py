a=input()
b=len(a)
#print(b)
if(b>7):
    for i in range(b):
        if(i%2==0):
         print(a[i])
elif(b<7):
    for j in range(b):
        if(j%2!=0):
             
           print(a[j])