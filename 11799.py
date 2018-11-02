x=int(input())
i=1
while i<=x:
    a=1
    y=input()
    y=y.split()
    for e in y:
        if int(e)>a:
            a=int(e)
    print ("Case "+str(i)+": "+str(a))
    i+=1
            
