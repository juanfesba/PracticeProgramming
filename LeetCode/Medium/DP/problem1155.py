
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        #ITERATIVE APPROACH
        if d==1:
            if target>f:
                return 0
            else:
                return 1
        DP=[[0 for e in range(d)] for ee in range(target+1)]
        for e in range(1,min(f+1,target+1)):
            DP[e][0]=1
        for j in range(1,d):
            for i in range(target+1):
                for nxt in range(1,f+1):
                    if i-nxt>0:
                        DP[i][j]+=DP[i-nxt][j-1]
                if DP[i][j]>1000000007:
                    DP[i][j]%=1000000007
                
        return DP[target][d-1]
        
        '''RECURSIVE APPROACH (time limit)
        DP={}
        def DPf(n,goal):
            check=DP.get((n,goal))
            if check:
                return DP[(n,goal)]
            if goal<1:return 0
            if(goal>n*f):return 0
            elif(n==1):
                return 1
            DP[(n,goal)]=0
            
            for e in range(1,f+1):
                DP[(n,goal)]=DP[(n,goal)]+DPf(n-1,goal-e)
            
            if(DP[(n,goal)]>(1000000007)):
                DP[(n,goal)]%=1000000007
            return DP[(n,goal)]
        
        return DPf(d,target)'''
