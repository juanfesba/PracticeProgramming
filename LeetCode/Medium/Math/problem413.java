class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        if(A.length<3){
            return 0;
        }
        int acc=1,dif=A[1]-A[0],i=1;
        int ans=0;
        while(i<A.length-1){
            if(A[i+1]-A[i]==dif){
                acc+=1;
            }
            else{
                ans+=calc(acc);
                acc=1;
                dif=A[i+1]-A[i];
            }
            i++;
        }
        if(acc!=1){
            ans+=calc(acc);
        }
        return ans;
    }
    public int calc(int n){
        if (n==1){
            return 0;
        }
        n-=1;
        return (n*(n+1))/2;
    }
}