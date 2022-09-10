
e=int(input("enter the no of people:- "))
ticket=0
ticket2=0
ticket3=0
for i in range(e):
    age=int(input("enter the age:- "))
    if(age<3):
        ticket=0
        
    if(3<=age<12):
        ticket2=100
    if(age>=12):
        ticket3=150
totalcost=ticket+ticket2+ticket3
print(totalcost)

    