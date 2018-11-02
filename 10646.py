def identificarcarta(x):
    if x=="T" or x=="J" or x=="Q" or x=="K" or x=="A":
        return 10
    else:
        return int(x)
t=1
casos=int(input())
while t<=casos:
    Y=0
    buscador=26
    x=input()
    x=x.split()
    card=identificarcarta(x[buscador][0])
    Y+=card
    buscador-=10-card+1
    card=identificarcarta(x[buscador][0])
    Y+=card
    buscador-=10-card+1
    card=identificarcarta(x[buscador][0])
    Y+=card
    buscador-=10-card
    if Y>(buscador):
        Y=x[32]
    else:
        Y=x[Y-1]
    print ("Case "+str(t)+": "+Y)
    t+=1
