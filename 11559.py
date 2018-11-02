x=input()
while x!="":
    x=x.split()
    N=int(x[0])
    B=int(x[1])
    H=int(x[2])
    W=int(x[3])
    i=0
    costofinal=B+1
    while i<H:
        p=int(input())
        oferta=N*p
        y=input()
        if costofinal>oferta:
            y=y.split()
            for e in y:
                if int(e)>N:
                    costofinal=oferta
        i+=1
    if costofinal<=B:
        print (costofinal)
    else:
        print ("stay home")
    x=input()
