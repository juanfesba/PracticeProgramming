class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solving it without division
        product=1
        left=[]
        right=[]
        for num in nums:
            product*=num
            left.append(product)
        product=1
        for e in range(len(nums)-1,-1,-1):
            product*=nums[e]
            right.insert(0,product)
            
        for i in range(len(nums)):
            if i==0:
                nums[i]=right[1]
            elif i==len(nums)-1:
                nums[i]=left[-2]
            else:
                nums[i]=left[i-1]*right[i+1]
        
        return nums
