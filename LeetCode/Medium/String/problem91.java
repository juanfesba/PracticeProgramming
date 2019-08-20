class Solution {
    
    public int numDecodings(String s) {
        int ans=1;
        int fibold=0;
        int fibcur=1;
        int tmp;
        boolean flag=false;
        
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='0'){
                if(fibold==0)return 0;
                else{
                    ans*=fibold;
                    fibold=0;
                    fibcur=1;
                }
            }
            if(s.charAt(i)=='1' || s.charAt(i)=='2'){
                tmp=fibcur;
                fibcur+=fibold;
                fibold=tmp;
                if(s.charAt(i)=='1')flag=true;
                else flag=false;
            }
            else if(flag || s.charAt(i)<'7'){
                ans*=fibold+fibcur;
                fibold=0;
                fibcur=1;
            }
            else{
                ans*=fibcur;
                fibold=0;
                fibcur=1;
            }
        }
        ans*=fibcur;
        return ans;
    }
}