import time
from tkinter import *
from linspace import *
from math import *
import matplotlib.pyplot as plt


#forced
root=Tk()
root.title("wave eq")
root.geometry("500x500")
graph=Canvas(root,width=300,height=200,bg="green")
graph.pack(fill="both",expand=True)

#f=k*d
n=100
y=[]
x=[]

for i in range(25):
    x.append(3*i)

for i in range(25):
    y.append(1/2*i)
    
for i in range(75):
    x.append(75+1/3*i)

for i in range(75):
    y.append(12.5-1/6*i)   


vy=[]
for i in range(len(x)):
    vy.append(0)

vx=[]
for i in range(len(x)):
    vx.append(0)

AL=0 #get arclength
#for i in range(len(x)):
    

k=1
m=10
dt=.2
fk=.21

zoom=4

j=0
while True:
    j+=1
    for i in range(1,len(x)-2):
        graph.create_line(zoom*x[i]+50,zoom*y[i]+250,zoom*x[i+1]+50,zoom*y[i+1]+250,fill="blue",width=2)
        
    for i in range(1,len(x)-1): #update y positions
        #y[0]=10*cos(j*pi/20)
        #y[len(x)-1]=20*cos(j*pi/200)
        d1=y[i]-y[i-1]
        d2=y[i]-y[i+1]
        F=-k*(d1+d2)
        fF=fk*vy[i]
        F=F-fF
        a=F/m
        vy[i]+=a*dt
        y[i]+=vy[i]*dt
        
        #x[0]=10*sin(j*pi/200)
        #y[len(x)-1]=20*cos(j*pi/200)
        d1=x[i]-x[i-1]
        d2=x[i]-x[i+1]
        F=-k*(d1+d2)
        fF=fk*vx[i]
        F=F-fF
        a=F/m
        vx[i]+=a*dt
        x[i]+=vx[i]*dt


        
    #print(vy[50])
    
    root.update()
    if j%2:
        graph.delete('all')

      

#show next: solve heat equation with cv2 lines making a video

