class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        potential=set([tree[0]])
        best=1
        current=1
        
        last=tree[0]
        lastC=1
        i=1
        
        while(i<len(tree)):
            lastC+=1
            current+=1
            if tree[i]!=last:
                potential.add(tree[i])
                last=tree[i]
                lastC=1
                i+=1
                break
            i+=1
        while(i<len(tree)):
            if tree[i]==last:
                lastC+=1
            else:
                if tree[i] not in potential:
                    best=max(best,current)
                    current=lastC
                    potential=set([tree[i],last])
                last=tree[i]
                lastC=1
            current+=1
            i+=1
        best=max(best,current)
        return best
