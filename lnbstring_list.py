from posixpath import split


sen=input("enter a string: ")
b=sen.split()
final=[]
for i in b:
    a=len(i)
    if(4<=a):
        final.append(i)
print("our input is :{}".format(sen))
print(final)
