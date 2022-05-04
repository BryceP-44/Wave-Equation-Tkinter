from turtle import *

#f=k*d

d=20
v=0
k=17.38
m=10
dt=.1


while True:
    f=-k*d
    a=f/m
    v+=a*dt
    d+=v*dt
    goto(0,d)
