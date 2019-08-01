class Solution {
    public boolean canJump(int[] nums) {
        if(nums.length<2){
            return true;
        }
        int i=1;
        int maxi=nums[0];
        while(i<=maxi && maxi<nums.length-1){
            maxi=Math.max(maxi,nums[i]+i);
            i++;
        }
        if(maxi>=nums.length-1){
            return true;
        }
        return false;
    }
}