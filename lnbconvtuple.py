x=()
n=int(input("enter no element in tuple"))
for i in range(0,n):
 x+=(int(input("enter input")),)
y=list(x)
z=input("enter a string")
for i in range(0,len(y)):
    a=len(y)
    
    if(i==1):
     y.insert(i,z)
     i=i+2
    if(i==3):
        y.insert(i,z)
        i=i+2
    if(i==5):
        y.insert(i,z)
        i=i+2
             
print(x)
print(y)
