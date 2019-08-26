class FreqStack:

    def __init__(self):
        self.frec=collections.defaultdict(int)
        self.stack=[]
        self.best=0
        self.count=0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.frec[x]+=1
        if self.frec[x]>self.best:
            self.best=self.frec[x]
            self.count=1
        elif self.frec[x]==self.best:
            self.count+=1

    def pop(self) -> int:
        index=0
        for i in range(len(self.stack)-1,-1,-1):
            if self.frec[self.stack[i]]==self.best:
                index=i
                self.frec[self.stack[i]]-=1
                self.count-=1
                if self.count==0:
                    self.best-=1
                    for e in self.frec.values():
                        if e==self.best:
                            self.count+=1
                
                break
        popped=self.stack[index]
        self.stack.pop(index)
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
