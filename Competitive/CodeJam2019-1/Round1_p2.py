from sys import stdin
from sys import stdout

T=int(stdin.readline())
i=0
while(i<T):
    N=int(stdin.readline())
    S=stdin.readline()
    ind=0
    ans=""
    
    for e in S:
        if(e=='E'):
            ans+='S'
        else:
            ans+='E'
    ans=ans[:-1]
    i+=1
    stdout.write("Case #"+str(i)+": "+ans+"\n")

stdout.close()
