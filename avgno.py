lst=[]
print("enter total no of element :") 
n=int(input())
b=0
for i in range(n):
    a=int(input())
    lst.append(a)
    
    b=b+a
avrage=b/n 
print("avrage of list element:{}".format(avrage))
print("{}".format(lst))
