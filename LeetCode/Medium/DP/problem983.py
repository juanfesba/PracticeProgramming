class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        DP={}
        
        def phi(current,i):
            nonlocal DP
            while i<len(days) and current>=days[i]:
                i+=1
            if i==len(days):
                return 0
            current=days[i]-1
            check=DP.get((current,i))
            if check!=None:
                return check
            DP[(current,i)]=ans=min( costs[0] + phi(current+1,i) , costs[1] + phi(current+7,i) , costs[2] + phi(current+30,i) )
            return ans
        
        return phi(days[0]-1,0)
        
