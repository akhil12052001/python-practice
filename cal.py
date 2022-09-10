from cmath import tan
import math as m


def mypro():
    print("which type calculator you want use")
    print("1.normal calculator")
    print("2.sciencetific calculator")
    x = int(input("enter your choice: "))

    if(x == 1):
        cal()
    elif(x == 2):
        cal2()
    else:
        print("please enter right choice")


def cal():
    print("1.addition")
    print("2.substrction")
    print("3.multiplication")
    print("4.divide")
    print("5.moduler")
    z = int(input("enter choice"))
    if(z == 1):
        add()
    elif(z == 2):
        sub()
    elif(z == 3):
        mul()
    elif(z == 4):
        div()
    elif (z == 5):
        mod()


def add():
    a = int(input("enter a input 1: "))
    b = int(input("enter a input 2: "))
    print("sum is: ", a+b)


def sub():
    a = int(input("enter a input 1: "))
    b = int(input("enter a input 2: "))
    print("sub is: ", a-b)


def mul():
    a = int(input("enter a input 1: "))
    b = int(input("enter a input 2: "))
    print("product is: ", a*b)


def div():
    a = int(input("enter a input 1: "))
    b = int(input("enter a input 2: "))
    print("ans is: ", a/b)


def mod():
    a = int(input("enter a input 1: "))
    b = int(input("enter a input 2: "))
    print("reminder is: ", a % b)


def cal2():
    print("1.sin()")
    print("2.cos()")
    print("3.tan()")
    print("4.mod()")
    print("5.power()")
    v = int(input("enter choice: "))
    if(v == 1):
        sin()
    elif(v == 2):
        cos()
    elif(v == 3):
        tan()
    elif(v == 4):
        mode()
    elif (v == 5):
        power()


def sin():
    a = int(input("enter a input 1: "))
    print("sin value is: ", m.sin(m.radians(a)))


def cos():
    a = int(input("enter a input 1: "))
    print("cos value is: ", m.cos(m.radians(a)))


def tan():
    a = int(input("enter a input 1: "))
    print("tan value is: ", m.tan(a))


def mode():
    a = int(input("enter a input 1: "))
    print("mod value is: ", m.modf(a))


def power():
    a = int(input("enter a input 1: "))
    b = int(input("enter a input 2: "))
    print("power value is: ", m.pow(a, b))


while(1):
    mypro()
