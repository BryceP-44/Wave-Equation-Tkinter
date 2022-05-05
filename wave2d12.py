from tkinter import *
from linspace import *
from math import *
import keyboard


#forced
root=Tk()
root.title("wave eq")
root.geometry("700x500")
graph=Canvas(root,width=300,height=200,bg="green")
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
m=10
dt=.5
fk=.6

zoom=4
shift=150

yoff=100
xoff=100

j=0
while True:
    j+=1
    for i in range(len(x)-2):
        graph.create_line(zoom*x[i]+shift,zoom*y[i]+250,zoom*x[i+1]+shift+xoff,zoom*y[i+1]+250+yoff,fill="blue",width=2)

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
        y[0]=20*sin(j*pi/100)
        x[len(x)-1]=100+10*cos(j*pi/250)
        y[len(x)-1]=20*cos(j*pi/200)
        
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

