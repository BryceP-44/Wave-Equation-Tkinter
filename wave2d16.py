from tkinter import *
from linspace import *
from math import *
import keyboard
import random


#forced
root=Tk()
root.title("wave eq")
root.geometry("700x500")
graph=Canvas(root,width=300,height=200,bg="black")
graph.pack(fill="both",expand=True)

#f=k*d
n=100
y=[]
x=[]

for i in range(100):
    x.append(0)
    y.append(0)


vy=[]
for i in range(len(x)):
    vy.append(0)

vx=[]
for i in range(len(x)):
    vx.append(0)

AL=0 #get arclength
#for i in range(len(x)):
    

k=1
m=20
ogl=4
dt=.5
fk=.6

zoom=8
shift=150

yoff=200
xoff=100

coff=100

cols=["blue","cyan","green","yellow","orange","red"]

j=0
while True:
    j+=1
    for i in range(len(x)-2):
        a=0
        b=1
        c=.9
        d=((x[i+1]-x[i])**2+(y[i+1]-y[i])**2)**.5
        if d>=b:
            a=1
        if d>=b+c:
            a=2
        if d>=b+c*2:
            a=3
        if d>=b+c*3:
            a=4
        if d>=b+c*4:
            a=5

        #print(a)
        graph.create_line(zoom*x[i]+shift,zoom*y[i]+400,zoom*x[i+1]+shift,zoom*y[i+1]+400,fill=cols[a],width=2)
        if i==50:
            graph.create_line(zoom*x[i]+shift,zoom*y[i]+400,zoom*x[i+1]+shift,zoom*y[i+1]+400,fill="white",width=2)
        #graph.create_line(zoom*x[i]+shift+coff,zoom*y[i]+400,zoom*x[i+1]+shift+coff,zoom*y[i+1]+400,fill=cols[a],width=2)
        #graph.create_line(zoom*x[i]+shift,zoom*y[i]+400,zoom*x[i+1]+shift+coff,zoom*y[i+1]+400,fill=cols[a],width=2)

        
        #graph.create_line(zoom*x[i]+shift,zoom*y[i]+250,zoom*x[i+1]+shift,zoom*y[i+1]+250+yoff,fill=cols[a],width=2)
        #graph.create_line(zoom*x[i]+shift+coff,zoom*y[i]+250,zoom*x[i+1]+shift+coff,zoom*y[i+1]+250+yoff,fill=cols[a],width=2)
        #graph.create_line(zoom*x[i]+shift+2*coff,zoom*y[i]+250,zoom*x[i+1]+shift+2*coff,zoom*y[i+1]+250+yoff,fill=cols[a],width=2)
        
        #graph.create_line(zoom*x[i]+shift+coff,zoom*y[i]+250,zoom*x[i+1]+shift+xoff+coff,zoom*y[i+1]+250+yoff,fill=cols[a],width=2)
        #graph.create_line(zoom*x[i]+shift+coff*2,zoom*y[i]+250,zoom*x[i+1]+shift+xoff+coff*2,zoom*y[i+1]+250+yoff,fill=cols[a+2],width=2)

    if keyboard.is_pressed('up arrow'):
        zoom+=.1
    if keyboard.is_pressed('down arrow'):
        if zoom>1:
            zoom-=.1
    if keyboard.is_pressed('right arrow'):
        shift-=10
    if keyboard.is_pressed('left arrow'):
        shift+=10
        
        
        
    for i in range(1,len(x)-1): #update y positions
        x[0]=5*cos(j*pi/150)
        y[0]=30*sin(j*pi/150)
        x[len(x)-1]=100+10*cos(j*pi/250)
        y[len(x)-1]=20*cos(j*pi/150)

        #d2=((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)**.5
        #F=-k*(d2-ogl)
        #v2=(
        #fF=fk*vy[i]
        
        d1=y[i]-y[i-1]
        d2=y[i]-y[i+1]
        F=-k*(d1+d2)
        fF=fk*vy[i]
        F=F-fF
        a=F/m
        vy[i]+=a*dt
        y[i]+=vy[i]*dt
        
        
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

