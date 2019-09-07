from sys import stdin
from sys import stdout

N=stdin.readline()
flag=True
while(len(N)>0):
    if not flag:
        stdout.write("\n")
    if flag:
        flag=False
    N=int(N)
    persons=stdin.readline().split()
    dic={}
    for e in persons:
        guy=stdin.readline().split()
        person=guy[0]
        money=int(guy[1])
        gives=int(guy[2])
        given=guy[3:3+gives]

        if gives==0:
            give=0
            spare=money
            spend=0
        else:
            give=money//gives
            spare=money%gives

        check=dic.get(person)
        if check==None:
            dic[person]=[spare,money]
        else:
            dic[person][0]+=spare
            dic[person][1]=money
        for g in given:
            check2=dic.get(g)
            if check2==None:
                dic[g]=[give,0]
            else:
                dic[g][0]+=give
    for p in persons:
        stdout.write(p)
        stdout.write(" ")
        stdout.write(str(dic[p][0]-dic[p][1]))
        stdout.write("\n")
        
    N=stdin.readline()

stdout.close()
        
