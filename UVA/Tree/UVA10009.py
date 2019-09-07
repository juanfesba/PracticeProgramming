from sys import stdin
from sys import stdout

T=int(stdin.readline())

'''
class cityNode():
    def __init__(self,city,parent):
        self.children=[]
        self.parent=parent
        self.city=city
    def addChild(self,child):
        self.children.append(child)
'''

flag=False
while(T>0):
    if flag:
        stdout.write("\n")
    else:
        flag=True
    stdin.readline()
    romanEmpire={}
    #cities={"R":cityNode("R",None)}
    parents={}
    roads,queries=[int(x) for x in stdin.readline().split()]
    for r in range(roads):
        parent,child=[x[0] for x in stdin.readline().split()]
        parents[child]=parent

        '''
        check=cities.get(parent)
        if check!=None:
            tmp=check
            #tmp.addChild(child)
        else:
            tmp=cityNode(parent,None)
            #tmp.addChild(child)
            cities[parent]=tmp
        check2=cities.get(child)
        if check2!=None:
            tmp2=check2
            if check2.parent==None:
                check2.parent=parent
        else:
            tmp2=cityNode(child,parent)
            cities[child]=tmp2
        '''

    for q in range(queries):
        parent,child=[x[0] for x in stdin.readline().split()]
        pathP=[parent]
        pathSet={parent}
        while(parent!="R"):
            parent=parents[parent]
            pathP.append(parent)
            pathSet.add(parent)
        childPath=[]
        while(child not in pathSet):
            childPath.insert(0,child)
            child=parents[child]
        ans=""
        for city in pathP:
            if child==city:
                ans+=city
                break
            ans+=city
        stdout.write(ans + "".join(childPath) + "\n")
        
    T-=1

stdout.close()
