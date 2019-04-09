from sys import stdin
from sys import stdout


def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



T=int(stdin.readline())
t=0
while(t<T):
    N,L=stdin.readline().strip().split()
    N=int(N)
    L=int(L)
    S=[int(x) for x in stdin.readline().strip().split()]

    dic={}
    ans=[None]*(L+1)

    first=S[0]
    i=1
    flag=0
    pending=0

    while(i<len(S)):
        
        last=S[i]
        if(not(flag)):
            if(first!=last):
                flag=gcd(first,last)

                #De A B C sacar B
                if dic.get(flag)==None:
                    dic[flag]=[i]
                else:
                    dic[flag].append(i)
                    
                #De A B C sacar A
                first=first/flag
                if dic.get(first)==None:
                    dic[first]=[i-1]
                else:
                    dic[first].append(i-1)
                    
                temp=True
                if(pending%2==0):
                    temp=False
                #Si A A A C
                if(flag==first):
                    while(pending>0):
                        dic[first].append(i-1-pending)
                        pending-=1
                #Si A B A C
                else:
                    while(pending>0):
                        if(temp):
                            if dic.get(flag)==None:
                                dic[flag]=[i]
                            else:
                                dic[flag].append(i-1-pending)
                        else:
                            if dic.get(first)==None:
                                dic[first]=[i-1-pending]
                            else:
                                dic[first].append(i-1-pending)
                        temp=not(temp)
                        pending-=1

                flag=last/flag
                if dic.get(flag)==None:
                    dic[flag]=[i+1]
                else:
                    dic[flag].append(i+1)
                
            else:
                pending+=1
            first=last
        else:
            flag=last/flag
            if dic.get(flag)==None:
                dic[flag]=[i+1]
            else:
                dic[flag].append(i+1)
            
        
        i+=1

    keys=sorted(dic.keys())
    ind=0
    for e in keys:
        for ee in dic[e]:
            ans[ee]=abc[ind]
        ind+=1
    t+=1
    stdout.write("Case #"+str(t)+": "+''.join(ans)+"\n")

#print('dic',dic)
#print('ans',ans)

stdout.close()

'''
1
103 3
217 1891 4819

1
10000 3
3292937 175597 18779

1
103 3
119 119 51

1
103 4
119 119 119 51

1
103 7
119 119 119 51 33 55 15

1
103 3
49 49 21

1
103 5
49 49 21 33 55

2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543
'''
