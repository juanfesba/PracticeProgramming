class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int)-> bool:
        
        DP={}
        
        def phi(state,current,player1):
            nonlocal DP
            check=DP.get(state)
            if check!=None:
                return check
            flag=False
            for integer in range(maxChoosableInteger,0,-1):
                available=state & 1<<integer
                if available==0:
                    newstate=state | 1<<integer
                    newcurrent=current+integer
                    if newcurrent>=desiredTotal:
                        if player1:
                            flag=True
                        break
                    else:
                        flag=phi(newstate,newcurrent,not player1)
                        if flag and player1:
                            break
                        if not flag and not player1:
                            break
            DP[state]=flag
            return flag
        
        return phi(0,0,True)
