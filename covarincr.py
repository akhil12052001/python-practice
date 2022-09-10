x=[2,3,4,5,6,7,8]
y=[4,9,16,25,36,49,64]
a=0
b=0
z=[]
w=[]
s=0
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
print(x)
print(y)
print(a1)
print(b2)
print(z)
print(w)
print(s)
cv=s/len(z)
print(cv)
if(cv>0):
    print("direct")
else:
    print("indirect")


