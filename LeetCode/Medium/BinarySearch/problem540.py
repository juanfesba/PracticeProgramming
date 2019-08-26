class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        low=0
        hi=len(nums)
        
        while low+1!=hi:
            
            mid=low+((hi-low)>>1)
            
            if mid==len(nums)-1:
                return nums[mid]
            if mid%2==0:
                if nums[mid+1]==nums[mid]:
                    low=mid
                else:
                    if nums[mid-1]!=nums[mid]:
                        return nums[mid]
                    hi=mid
            else:
                if nums[mid+1]!=nums[mid]:
                    low=mid
                else:
                    hi=mid
        
        return nums[low]
