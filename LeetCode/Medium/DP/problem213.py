class Solution:
    def rob(self, nums: List[int]) -> int:
        size=len(nums)
        if size==0:
            return 0
        DP={}
        def phi(n,first):
            nonlocal size,DP
            if n>=size:
                return 0
            if n==size-1:
                if first:
                    return 0
                return nums[size-1]
            check=DP.get((n,first))
            if check!=None:
                return check
            ans=nums[n]
            ans+=max( phi(n+2,first) , phi(n+3,first) )
            
            DP[(n,first)]=ans
            return ans
            
        ans=max( nums[0]+phi(2,True) , nums[0]+phi(3,True) , phi(1,False) , phi(2,False) )
        
        return ans
            
