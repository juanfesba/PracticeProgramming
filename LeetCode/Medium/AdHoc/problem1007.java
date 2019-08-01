class Solution {
    public int minDominoRotations(int[] A, int[] B) {
        int max=A.length;
        int ans=-1;
        

        int offset=0;
        
        int optA=A[0];
        int optB=B[0];
        int optA_A=0,optA_B=0,optB_A=0,optB_B=0;
        int optC=0;  //
        
        if(optA==optB){
            offset=1;
            optC=optA;
        }
        else{
            optA_A=1;
            optB_B=1;
        }
        
        int readA,readB;
        for(int i=1;i<max;i++){
            readA=A[i];readB=B[i];
            
            if(offset!=0){
                if(readA==readB){
                    if(readA!=optC)return -1;
                    //offset+=1;
                }
                else if(readA==optC)optA_A+=1;
                else if(readB==optC)optA_B+=1;
                else return -1;
            }
            else{
                if(readA==readB){
                    offset+=1;
                    optC=readA;
                    if(readB==optB){
                        optA_A=optB_A;
                        optA_B=optB_B;
                    }
                }
                else if(optA!=readA && optA!=readB){
                    if(optB!=readA && optB!=readB)return -1;
                    offset+=1;
                    optA_A=optB_A;
                    optA_B=optB_B;
                    optC=optB;
                    if(readA==optC)optA_A+=1;
                    else optA_B+=1;
                }
                else if(optB!=readA && optB!=readB){
                    offset+=1;
                    optC=optA;
                    if(readA==optC)optA_A+=1;
                    else optA_B+=1;
                }
                else{
                    if(readA==optA)optA_A+=1;
                    else if(readA==optB)optB_A+=1;
                    if(readB==optA)optA_B+=1;
                    else if(readB==optB)optB_B+=1;
                }
            }
        }
        if(offset!=0){
            ans=Math.min(optA_A,optA_B);
        }
        else{
            optA_A=Math.min(optA_A,optA_B);
            optB_A=Math.min(optB_A,optB_B);
            ans=Math.min(optA_A,optB_A);
        }
        return ans;
    }
}