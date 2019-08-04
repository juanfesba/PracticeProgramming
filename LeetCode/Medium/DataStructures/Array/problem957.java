class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        int[] tmp=cells.clone();
        tmp[0]=0;
        tmp[7]=0;
        
        for(int i=1;i<7;i++){
            if(cells[i-1]==cells[i+1])tmp[i]=1;
            else tmp[i]=0;
        }
        N-=1;
        if(N==0)return tmp;
        int[] ans=tmp.clone();
        cells=tmp.clone();
        int mod=0;
        while(N>0){
            for(int i=1;i<7;i++){
                if(cells[i-1]==cells[i+1])tmp[i]=1;
                else tmp[i]=0;
            }
            cells=tmp.clone();
            mod++;
            N--;
            if(Arrays.equals(ans,cells))break;
        }
        if(N==0)return cells;
        N=N%mod;
        while(N>0){
            for(int i=1;i<7;i++){
                if(cells[i-1]==cells[i+1])tmp[i]=1;
                else tmp[i]=0;
            }
            cells=tmp.clone();
            N--;
        }
        return cells;
    }
}