from sys import stdin
from math import sqrt

def distanciapunto(nx,ny,nx1,ny1):
    dist=sqrt((ny1-ny)**2+(nx1-nx)**2)
    return dist

def distanciasegmento(nx1,ny1,nx2,ny2,nx,ny):
    dist=1000
    if (ny2-ny1)==0:
        if ((nx>=nx1) and (nx<=nx2))or((nx>=nx2) and (nx<=nx1)):
            dist=abs(ny1-ny)
        return dist
    if (nx2-nx1)==0:
        if ((ny>=ny1) and (ny<=ny2))or((ny>=ny2) and (ny<=ny1)):
            dist=abs(nx1-nx)
        return dist
    mseg=(ny2-ny1)/(nx2-nx1)
    bseg=ny1-mseg*nx1
    mcen=-(1/mseg)
    bcen=ny-mcen*nx
    xinter=((bcen-bseg)/(mseg-mcen))
    yinter=mseg*xinter+bseg
    if ((xinter>=nx1 and xinter<=nx2) or (xinter>=nx2 and xinter<=nx1)) and ((yinter>=ny1 and yinter<=ny2) or (yinter>=ny2 and yinter<=ny1)):
        dist=distanciapunto(x,y,xinter,yinter)
    return dist
    
    


n=stdin.readline()
while n!='*\n':
    n=int(n)-1
    xy=stdin.readline().split()
    x=int(xy[0])
    y=int(xy[1])
    xy=stdin.readline().split()
    xfirst=int(xy[0])
    yfirst=int(xy[1])
    x1=xfirst
    y1=yfirst
    distancia=1000
    while n>0:
        xy=stdin.readline().split()
        x2=int(xy[0])
        y2=int(xy[1])
        newdist=distanciapunto(x,y,x1,y1)
        if newdist<=distancia:
            distancia=newdist
        newdist=distanciasegmento(x1,y1,x2,y2,x,y)
        if newdist<=distancia:
            distancia=newdist
            
        x1=x2
        y1=y2   
        n-=1
    newdist=distanciapunto(x,y,x1,y1)
    if newdist<=distancia:
        distancia=newdist
    newdist=distanciasegmento(x1,y1,xfirst,yfirst,x,y)
    if newdist<=distancia:
        distancia=newdist
    print(format(distancia, '.3f'))
    n=stdin.readline()
