class Solution(object):
    def PredictTheWinner(self, nums):
        DP={}
        def DPRec(i,j,turn):
            if(i==j):return turn,nums[i]
            elif(i+1==j):
                return turn or nums[i]-nums[j]==0,max(nums[i],nums[j])-min(nums[i],nums[j])
            
            check=DP.get((i+1,j))
            if(check!=None):left,leftx=DP[(i+1,j)]
            else: left,leftx=DP[(i+1,j)]=DPRec(i+1,j,not(turn))
            
            check=DP.get((i,j-1))
            if(check!=None):right,rightx=DP[(i,j-1)]
            else: right,rightx=DP[(i,j-1)]=DPRec(i,j-1,not(turn))
                
            if(turn==left):leftx+=nums[i]
            elif(nums[i]>leftx):
                left=turn
                leftx=nums[i]-leftx
            elif(nums[i]<leftx):
                leftx-=nums[i]
            else:
                left=True
                leftx=0

            if(turn==right):rightx+=nums[j]
            elif(nums[j]>rightx):
                right=turn
                rightx=nums[j]-rightx
            elif(nums[j]<rightx):
                rightx-=nums[j]
            else:
                right=True
                rightx=0
                
            if(left==turn and right==turn):return turn,max(leftx,rightx)
            elif(left!=turn and right!=turn):return left,min(leftx,rightx)
            elif(left==turn):return left,leftx
            else: return right,rightx
        
        return DPRec(0,len(nums)-1,True)[0]
        """
        :type nums: List[int]
        :rtype: bool
        """
        