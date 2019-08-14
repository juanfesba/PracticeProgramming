class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        pairs=[]
        
        for i in range(len(workers)):
            for j in range(len(bikes)):
                pairs.append((workers[i],bikes[j],i,j))
        
        def Manhattan(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        pairs.sort(key = lambda P: (Manhattan(P[0],P[1]),P[2],P[3]))
        
        ans=[-1]*len(workers)
        bikesMask=[-1]*len(bikes)
        
        count=len(workers)
        for pair in pairs:
            if(ans[pair[2]]==-1 and bikesMask[pair[3]]==-1):
                ans[pair[2]]=pair[3]
                bikesMask[pair[3]]=1
                count-=1
                if count==0:break
        
        return ans
