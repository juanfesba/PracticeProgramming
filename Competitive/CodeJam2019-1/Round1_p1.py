from sys import stdin
from sys import stdout

T=int(stdin.readline())
i=0
while(i<T):
    N=int(stdin.readline())
    A=0
    B=0
    res=N%10
    N//=10
    factor=1
    while(N>0):
        if(res==0):
            pass
        elif(res!=4):
            A+=res*factor
        else:
            A+=2*factor
            B+=2*factor
        factor*=10
        res=N%10
        N//=10
        #print("N",N,res,factor,"A",A,"B",B)
    if(res!=4):
        A+=res*factor
    else:
        A+=2*factor
        B+=2*factor
    i+=1
    stdout.write("Case #"+str(i)+": "+str(A)+" "+str(B)+"\n")

stdout.close()
