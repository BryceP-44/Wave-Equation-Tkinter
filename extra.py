import time
from tkinter import *

root=Tk()
root.title("wave eq")
root.geometry("500x500")
graph=Canvas(root,width=300,height=200,bg="green")
graph.pack(fill="both",expand=True)

#f=k*d
d=200
v=0
#k=17.38
k=100
m=10
dt=.008
x=0

for i in range(100000):
    dog=d
    x+=dt
    f=-k*d
    a=f/m
    v+=a*dt
    d+=v*dt
    graph.create_line(x-dt,dog,x,d,fill="blue")
    root.update()

    
    

