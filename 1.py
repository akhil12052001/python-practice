n=int(input())
lst=[]
for i in range(1,n+1):
    a=str(i)
    lst.append(a)
print( lst)
a=''
for j in range(0,n):
    a=a+lst[j]
    
print(a)
