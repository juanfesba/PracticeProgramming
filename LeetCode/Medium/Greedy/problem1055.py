class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sparse=collections.defaultdict(list)
        pos={}
        for i in range(len(source)):
            char=source[i]
            sparse[char].append(i)
        
        for key in sparse.keys():
            pos[key]=0
        
        ans=1
        cur=0
        for char in target:
            if sparse.get(char)==None:
                return -1
            
            if pos[char]==len(sparse[char]):
                ans+=1
                cur=0
                for key in pos.keys():
                    pos[key]=0
            while(cur>sparse[char][pos[char]]):
                pos[char]+=1
                if pos[char]==len(sparse[char]):
                    ans+=1
                    cur=0
                    for key in pos.keys():
                        pos[key]=0
            cur=sparse[char][pos[char]]
            pos[char]+=1
            
        return ans
