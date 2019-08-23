class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if N<3 or (N==3 and r==1 and c==1):
            if K==0:
                return 1.0
            else:
                return 0.0
        if N==3:
            return (0.125**K)*(2**K)
        
        current=collections.defaultdict(int)
        current[(r,c)]=1
        
        
            
        #next
        def calcnext(row,col,times):
            if current[(row,col)]==0:
                return
            current[(row,col)]-=times
            if row==0:
                if col<N-2:
                    current[(row+1,col+2)]+=times
                if col<N-1:
                    current[(row+2,col+1)]+=times
                if col>0:
                    current[(row+2,col-1)]+=times
                if col>1:
                    current[(row+1,col-2)]+=times
            elif row==N-1:
                if col<N-2:
                    current[(row-1,col+2)]+=times
                if col<N-1:
                    current[(row-2,col+1)]+=times
                if col>0:
                    current[(row-2,col-1)]+=times
                if col>1:
                    current[(row-1,col-2)]+=times
            elif row==1:
                if col<N-2:
                    current[(row+1,col+2)]+=times
                    current[(row-1,col+2)]+=times
                if col<N-1:
                    current[(row+2,col+1)]+=times
                if col>0:
                    current[(row+2,col-1)]+=times
                if col>1:
                    current[(row+1,col-2)]+=times
                    current[(row-1,col-2)]+=times
            elif row==N-2:
                if col<N-2:
                    current[(row+1,col+2)]+=times
                    current[(row-1,col+2)]+=times
                if col<N-1:
                    current[(row-2,col+1)]+=times
                if col>0:
                    current[(row-2,col-1)]+=times
                if col>1:
                    current[(row+1,col-2)]+=times
                    current[(row-1,col-2)]+=times
            else:
                if col<N-2:
                    current[(row+1,col+2)]+=times
                    current[(row-1,col+2)]+=times
                if col<N-1:
                    current[(row-2,col+1)]+=times
                    current[(row+2,col+1)]+=times
                if col>0:
                    current[(row-2,col-1)]+=times
                    current[(row+2,col-1)]+=times
                if col>1:
                    current[(row+1,col-2)]+=times
                    current[(row-1,col-2)]+=times
        

        items=current.copy().items()
        for e in range(K):
            for item in items:
                calcnext(item[0][0],item[0][1],item[1])
            items=current.copy().items()
        ans=0
        for key in current.keys():
            ans+=current[key]
        
        
        return (0.125**K)*(ans)
                        
                        
                        
