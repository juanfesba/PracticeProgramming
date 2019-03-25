import java.util.LinkedList;
import java.util.Iterator;

class Solution {
    
    /*public class struct{
        public int i;
        public int flag;
        
        struct(int ni,int nflag){
            flag=nflag;
            i=ni;
        }
    }*/
    
    public int minKBitFlips(int[] A, int K) {
        LinkedList<Integer> range=new LinkedList<Integer>();
        
        //range.add(new struct(0,1));
        range.add(A.length-1);
        ListIterator<Integer> itr=range.listIterator();
        
        int ele=itr.next();
        ele=itr.next();
        
        int ans=-1;
        int i=0;
        int flag=0;
        
        int ref;
        
        while(i<A.length){ //recordar que realmente es hasta A.lenght-K
            if(i>A.length-K){
                if (A[i]-flag==0){
                    ans=-1;
                    break;
                }
            }
            else{
                if(i>ele){
                    ele=itr.next();
                    flag=1-flag;
                }
                if (A[i]-flag==0){
                    ans+=1;
                    if(K>1){
                        flag=1-flag;
                        ref=i+K-1;
                        if(ref<ele){
                            itr.add(ele);
                            ele=ref;
                        }
                        else{
                            if(ref>ele){
                                itr.add(ref);
                            }
                        }
                    }
                }
            }
            i++;
        }
        
        if (ans!=-1){
            ans+=1;
        }
        
        return ans;
    }
}