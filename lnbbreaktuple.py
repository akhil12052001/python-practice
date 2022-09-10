x=()
n=int(input("enter no of elements"))
for i in range(n):
 x+=(int(input("enter input")),)
y=list(x)
a=[]
b=[]
c=len(y)
z=len(y)//2
print(z)
for i in range(c):
    if(0<=i<=z):
     a.append(y[i])
    if(z<i<=c):
     b.append(y[i])
print(y)
print(tuple(a))
print(tuple(b))
apple=mango