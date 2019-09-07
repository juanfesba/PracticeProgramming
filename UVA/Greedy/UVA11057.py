from sys import stdin
from sys import stdout

mod=0
for line in stdin:
    line=line.strip()
    mod+=1
    ans=(0,0)
    best=float("inf")
    if mod==4:
        mod=0
        continue
    if mod==1:
        N=int(line)
    elif mod==2:
        prices=[int(x) for x in line.split()]
    else:
        goal=int(line)

        dic={}
        for price in prices:
            check=dic.get(price)
            if check!=None:
                if check<best:
                    best=check
                    ans=(price,goal-price)
            dic[goal-price]=abs(abs(goal-price)-price)
        stdout.write("Peter should buy books whose prices are ")
        stdout.write(str(min(ans)))
        stdout.write(" and ")
        stdout.write(str(max(ans)))
        stdout.write(".\n\n")

stdout.close()
