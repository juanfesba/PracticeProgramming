x=input()
while x!="0 0":
    x=x.split()
    x0=int(x[0])
    x1=int(x[1])
    if x0==0 or x1==0:
        x=0
    elif x0==1:
        x=x[1]
    elif x1==1:
        x=x0
    elif x0==2:
        if x1<5:
            x=4
        elif (x1%4)==0:
            x=x1
        elif ((x1-1)%4)==0:
            x=x1+1
        else:
            x=int(x1/4)*4+4
    elif x1==2:
        if x0<5:
            x=4
        elif (x0%4)==0:
            x=x0
        elif ((x0-1)%4)==0:
            x=x0+1
        else:
            x=int(x0/4)*4+4
    elif x0%2==0 or x1%2==0:
        x=int((x0*x1)/2 )
    else:
        x=int((x0*x1+1)/2)
    print (str(x)+" knights may be placed on a "+str(x0)+" row "+str(x1)+" column board.")
    x=input()
