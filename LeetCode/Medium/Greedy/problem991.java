class Solution {
    public int brokenCalc(int X, int Y) {
        int ans=0;
        if(X>Y){
            return X-Y;
        }
        if(X==Y){
            return 0;
        }
        else if(Y%2==1){
            Y+=1;
            ans+=1;
        }
        while(Y>X){
            Y/=2;
            ans+=1;
            if(X==Y){
                return ans;
            }
            if(X>Y){
                return ans+X-Y;
            }
            if(Y%2==1){
                Y+=1;
                ans+=1;
            }
        }
        return ans;
    }
}