from logging import exception
from tkinter import RAISED


n=int(input("enter value"))
if(n==0):
    raise Exception("the value is zero")
else:
    print("{}/2".format(n))