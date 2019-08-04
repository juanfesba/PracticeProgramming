class Solution {
    public int[][] DP;
    public int[] Nums;
    public int[] Acc;
    
    public int DPRec(int n,int k){
        if(n==0){
            if(Math.abs(k)==Nums[0]){
                if(Nums[0]==0)return 2;
                else return 1;
            }
            else return 0;
        }
        if(Math.abs(k)>Acc[n])return 0;
        if(DP[n][k+1000]!=-1)return DP[n][k+1000];
        DP[n][k+1000]=DPRec(n-1,k+Nums[n])+DPRec(n-1,k-Nums[n]);
        return DP[n][k+1000];
    }
    
    public int findTargetSumWays(int[] nums, int S) {
        int[] acc=new int[nums.length];
        acc[0]=nums[0];
        for(int i=1;i<nums.length;i++)acc[i]=nums[i]+acc[i-1];
        Acc=acc;
        Nums=nums;
        DP=new int[nums.length+1][2005];
        for(int i=0;i<nums.length;i++)Arrays.fill(DP[i],-1);
        
        
        return DPRec(nums.length-1,S);
    }
}