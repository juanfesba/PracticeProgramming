class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        maxL=max(len(A),len(B))
        ans=[]
        lists=[A,B]
        i=0
        j=0
        while(True):
            if(i==len(A) or j==len(B)):break
            
            if(A[i][0]<=B[j][0]):
                minIndex=1
                x=j
            else:
                minIndex=0
                x=i
                
            if(A[i][1]<=B[j][1]):
                maxIndex=0
                y=i
            else:
                maxIndex=1
                y=j
            
            if(lists[maxIndex][y][1]>=lists[minIndex][x][0]):
                ans.append([lists[minIndex][x][0],lists[maxIndex][y][1]])
            
            if(maxIndex):j+=1
            else: i+=1
        return ans