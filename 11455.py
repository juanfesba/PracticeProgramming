from sys import stdin
from sys import stdout

T=int(stdin.readline())
for e in range(T):
    line=stdin.readline().strip().split()

    for e in range(4):
        line[e]=int(line[e])

    flagcua=False
    flagrec=False
    flagqua=False

    if line[0]==line[1]:
        if line[2]==line[3]:
            flagrec=True
            if line[0]==line[2]:
                flagcua=True

    if line[0]==line[2]:
        if line[1]==line[3]:
            flagrec=True
            if line[0]==line[1]:
                flagcua=True

    if line[0]==line[3]:
        if line[1]==line[2]:
            flagrec=True
            if line[0]==line[2]:
                flagcua=True

    if flagcua:
        stdout.write('square\n')
        continue
    if flagrec:
        stdout.write('rectangle\n')
        continue

    check=line[0]
    ch=0
    
    if line[1]>check:
        check=line[1]
        ch=1
    if line[2]>check:
        check=line[2]
        ch=2
    if line[3]>check:
        check=line[3]
        ch=3

    if ch==0:
        if check>(line[1]+line[2]+line[3]):
            stdout.write('banana\n')
        else:
            stdout.write('quadrangle\n')
    elif ch==1:
        if check>(line[0]+line[2]+line[3]):
            stdout.write('banana\n')
        else:
            stdout.write('quadrangle\n')
    elif ch==2:
        if check>(line[0]+line[1]+line[3]):
            stdout.write('banana\n')
        else:
            stdout.write('quadrangle\n')
    elif ch==3:
        if check>(line[0]+line[1]+line[2]):
            stdout.write('banana\n')
        else:
            stdout.write('quadrangle\n')

stdout.close()
