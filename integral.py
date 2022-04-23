
def linspace(start,end,N):
    a=start
    b=end
    n=N
    q=(b-a)/n
    cont=1
    u=a
    x=[]
    while cont==1:
        x.append(round(u,len(str(N))+1))
        u+=q
        if u>b and q>0:
            cont=0
        if u<a and q<0:
            cont=0
    return x

def integral(integrand,x,a,b):
    summ,n=0,50000
    xlist=linspace(a,b,n)
    q=(b-a)/n
    for i in range(len(xlist)):
        expr=integrand.replace(x,str(xlist[i]))
        summ+=eval(expr)*q
    return summ
    

print(integral("3*x","x",-1,1))
