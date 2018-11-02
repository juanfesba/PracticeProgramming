from sys import stdin
from sys import stdout
from math import sqrt

def distanciapunto(nx,ny,nx1,ny1):
    dist=sqrt((ny1-ny)**2+(nx1-nx)**2)
    return dist

def orientacion(nx,ny,nx1,ny1,nx2,ny2):
    if (nx-nx2)*(ny1-ny2)-(ny-ny2)*(nx1-nx2)>0:
        return True
    return False

entradas=[]
entrada=[float(x) for x in stdin.readline().strip().split()[1:]]
while len(entrada)!=0:
    entradas.append(entrada)
    entrada=[float(x) for x in stdin.readline().strip().split()[1:]]

px,py=[float(x) for x in stdin.readline().strip().split()]
i=1
while px!=9999.9 and  py!=9999.9:
    j=1
    flag=True
    for e in entradas:
        if len(e)==4:
            if px>e[0] and px<e[2] and py<e[1] and py>e[3]:
                stdout.write('Point '+str(i)+' is contained in figure '+str(j)+'\n')
                flag=False
        elif len(e)==3:
            if distanciapunto(px,py,e[0],e[1])<e[2]:
                stdout.write('Point '+str(i)+' is contained in figure '+str(j)+'\n')
                flag=False
        else:
            if orientacion(e[0],e[1],e[2],e[3],e[4],e[5]):
                if orientacion(e[0],e[1],e[2],e[3],px,py):
                    if orientacion(e[2],e[3],e[4],e[5],px,py):
                        if orientacion(e[4],e[5],e[0],e[1],px,py):
                            stdout.write('Point '+str(i)+' is contained in figure '+str(j)+'\n')
                            flag=False
            else:
                if not(orientacion(e[0],e[1],e[2],e[3],px,py)):
                    if not(orientacion(e[2],e[3],e[4],e[5],px,py)):
                        if not(orientacion(e[4],e[5],e[0],e[1],px,py)):
                            stdout.write('Point '+str(i)+' is contained in figure '+str(j)+'\n')
                            flag=False
        j+=1
    if flag:
        stdout.write('Point '+str(i)+' is not contained in any figure\n')
    px,py=[float(x) for x in stdin.readline().strip().split()]
    i+=1

stdout.close()
