class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        Appear={}
        i=0
        for char in S:
            check=Appear.get(char)
            if check:
                check[1]=i
            else:
                Appear[char]=[i,i]
            i+=1
        
        count=0
        ans=[]
        limit=-1
        for i in range(len(S)):
            start,end=Appear[S[i]]
            count+=1
            if start==i:
                limit=max(end,limit)
            if limit==i:
                ans.append(count)
                count=0
                
        return ans
