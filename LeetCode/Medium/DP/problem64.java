class Solution {
    public int minPathSum(int[][] grid) {
        int best;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                best=Integer.MAX_VALUE;
                if(i!=0)best=Math.min(best,grid[i-1][j]);
                if(j!=0)best=Math.min(best,grid[i][j-1]);
                if(best!=Integer.MAX_VALUE)grid[i][j]+=best;
            }
        }
        return grid[grid.length-1][grid[0].length-1];
    }
}