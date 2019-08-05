class Solution {
    public int maximalSquare(char[][] matrix) {
        if(matrix.length==0)return 0;
        int h=matrix.length;int w=matrix[0].length;
        int ans=0;
        int[][] acc=new int[h][w];
        
        for(int i=0;i<w;i++){
            if(matrix[0][i]=='1'){
                ans=1;
                acc[0][i]=1;
            }
            else acc[0][i]=0;
        }
        int current;boolean flag;
        for(int i=1;i<h;i++){
            current=0;flag=true;
            for(int j=0;j<w;j++){
                if(matrix[i][j]=='0'){
                    current=0;
                    continue;
                }
                else{
                    acc[i][j]=acc[i-1][j]+1;
                }
                if(flag){
                    if(acc[i][j]>ans)current+=1;
                    else current=0;
                    
                    if(current==ans+1){
                        flag=false;
                        ans=current;
                    }
                }
            }
        }
        return ans*ans;
    }
}