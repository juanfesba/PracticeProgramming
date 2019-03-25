class Solution {
    public String strWithout3a3b(int A, int B) {
        String ans="";
        boolean flag=true;
        if(A==0 && B==0){
            return "";
        }
        if(A==1 && B==0){
            return "a";
        }
        if(A==0 && B==1){
            return "b";
        }
        if(A==1 && B==1){
            return "ab";
        }
        if(A==B){
            while(A>0){
                ans=ans.concat("ba");
                A-=1;
            }
            return ans;
        }
        else if(A>B){
            while(A>1 && flag){
                ans=ans.concat("aa");
                A-=2;
                if(B!=0){
                    ans=ans.concat("b");
                    B-=1;
                }
                if(A==B){
                    flag=false;
                }
            }
            if(!flag){
                while(A>0){
                    ans=ans.concat("ab");
                    A-=1;
                }
            }
            else if(A==1){
                ans=ans.concat("a");
            }
            return ans;
            
        }
        else{
            while(B>1 && flag){
                ans=ans.concat("bb");
                B-=2;
                if(A!=0){
                    ans=ans.concat("a");
                    A-=1;
                }
                if(A==B){
                    flag=false;
                }
            }
            if(!flag){
                while(A>0){
                    ans=ans.concat("ba");
                    A-=1;
                }
            }
            else if(B==1){
                ans=ans.concat("b");
            }
            return ans;
            
        }
    }
}