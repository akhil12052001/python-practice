import binascii
from posixpath import split
import string
from tkinter import Y


print("* enter value between 10 and 20")
n=int(input())
b=[]
if(10<=n<=20):
  a=bin(n)
  b.append(a)
c=tuple(b)
d=c[0]
print(d)
x=d[5]
y=d[4]
z=x and y
 
j=x or y
tpl1=(z,j)

  
#bin=z+j
#print(bin)
print(tpl1)
  



  
  
  
    
            
           


