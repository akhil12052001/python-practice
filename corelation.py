x=[12400,16500,17200,18000,21000]
y=[60,100,300,350,440]
a=0
b=0
z=[]
w=[]
s=0
x1=0
x2=0
for i in range(len(x)):
    a=a+x[i]
for j in range(len(y)):
    b=b+y[j]
a1=a/len(x)
b2=b/len(y)
for k in range(len(x)):
    c=x[k]-a1  
    z.append(c)
    
for l in range(len(y)):
    d=y[l]-b2
    w.append(d)
for m in range(len(z)):
    s=s+z[m]*w[m]
for o in range(len(z)):
    x1=x1+z[o]*z[o]
    x2=x2+w[o]*w[o] 
    sq=x1*x2**0.5

print(x)
print(y)
print(a1)
print(b2)
print(z)
print(w)
print(s)
cv=s/sq
print(cv)
if(-1<cv<1):
    if(cv==1):
     print("direct")
else:

    print("indirect")


