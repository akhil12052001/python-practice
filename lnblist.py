L1=[]
L2=[]
L3=[]
n=int(input())
for i in range(n):
    a=int(input("L1:- "))
    L1.append(a)
for i in range(n):
    b=int(input("L2:- "))
    L2.append(b)
    if(i%2==0):
        L3.append(L1[i])
    if(i%2!=0):
        L3.append(L2[i])
print(L3)





