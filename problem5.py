e=int(input("no.of employee:- "))
w=int(input("no.of working days:- "))
data=[]
count=0
for i in range(1,w):
    if(i<=w<=10):
        a=input()
        data.append(a)
for i in range(1,w):
    if(a=='P'):
        count=count+i

print(data)
print(count)      

