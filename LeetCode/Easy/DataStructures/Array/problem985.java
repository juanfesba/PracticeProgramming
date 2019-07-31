class Solution {
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {
        int val,index,parity,oldVal;
        int even=0;
        int[] ans=new int[queries.length];
        for(int i=0;i<A.length;i++){
            if(A[i]%2==0)even+=A[i];
        }
        for(int j=0;j<queries.length;j++){
            val=queries[j][0];
            index=queries[j][1];
            oldVal=A[index];
            parity=Math.abs(A[index])%2;
            A[index]+=val;
            if( parity==1 && Math.abs(val)%2==1 )even+=A[index];
            else if( parity==0 ){
                if ( Math.abs(val)%2==0 ) even+=val;
                else even-=oldVal;
            }
            ans[j]=even;
        }
        return ans;
    }
}