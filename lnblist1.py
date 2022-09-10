l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
for i in range(0,20):
    a=int(input("enter a input value"))
    if(1<=a<=20):
     l1.append(a)
    #else:
        #continue
    #print(l1)
    
print(len(l1))

for j in range(0,len(l1)):
    if(0<=j<5):
        c=l1[j]
        l2.append(c)
    if(len(l1)-5<=j<len(l1)):
     d=l1[j]
     l2.append(d)
for k in range(0,len(l2)):
    e=l2[k]*l2[k]
    l3.append(e)
for l in range(0,len(l3)):
    if(0<=l<2):
        x=l3[l]
        l4.append(x)
    if(2<=l<5):
        y=l3[l]
        l5.append(y)
    if(5<=l<10):
        z=l3[l]
        l6.append(z)
   

    

    
print("list1 is:{}".format(l1))
print("list2 is:{}".format(l2))
print("list3 is:{}".format(l3))
print("list4(splitted) is:{}".format(l4))
print("list5 (spllitted) is:{}".format(l5))
print("list6 (splitted )is:{}".format(l6))
#print("list7 remain is:{}".format(l7))  
