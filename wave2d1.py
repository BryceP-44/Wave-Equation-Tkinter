import time
from tkinter import *
from linspace import *
from math import *

root=Tk()
root.title("wave eq")
root.geometry("500x500")
graph=Canvas(root,width=300,height=200,bg="green")
graph.pack(fill="both",expand=True)

#f=k*d
n=100000
x=linspace(0,1000,n)
y=[]
for i in range(len(x)):
    y.append(sin(pi/10*x[i]))



k=.1
m=10
dt=.1
x=0



while True:
    for i in range(1,len(x-1)):
        d1=y[i]-y[i-1]
        d2=y[i+1]-y[i]
        fy=k*(d1+d2)
        a=
    
    
    
    graph.create_line(x-dt,dog+250,x,d+250,fill="blue",width=5)
    root.update()

      
    

