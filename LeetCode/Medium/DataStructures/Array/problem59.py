class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        pattern=[n,n-1,n-1,n-2]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        ans=[[1 for _ in range(n)] for _ in range(n)]
        row,col=0,0
        val=1
        
        tmppat=pattern[:]
        iterator=0
        
        while True:
            if pattern[iterator]<1:
                break
            ans[row][col]=val
            pattern[iterator]-=1
            if pattern[iterator]==0:
                iterator+=1
                if iterator==4:
                    iterator=0
                    tmppat[0]-=2
                    tmppat[1]-=2
                    tmppat[2]-=2
                    tmppat[3]-=2
                    pattern=tmppat[:]
            dx,dy=direction[iterator]
            row+=dx
            col+=dy
            
            val+=1
        
        return ans
