public static int minKBitFlips(int[] A, int K) {
        LinkedList<Integer> range=new LinkedList<Integer>();
        
        range.add(A.length-1);
        
        int ans=0;
        int i=0;
        int j=0;
        int flag=0;
        int ref;
        int ele=range.get(j);
        int ref2=0;
        
        while(i<A.length){
            if(i>A.length-K){
                if(i>ele){
                    j+=1;
                    ele=range.get(j);
                    flag=1-flag;
                }
                if (A[i]-flag==0){
                    ans=-1;
                    break;
                }
            }
            else{
                if(i>ele){
                    j+=1;
                    ele=range.get(j);
                    flag=1-flag;
                    ref2-=1;
                }
                if (A[i]-flag==0){
                    ans+=1;
                    if(K>1){
                        flag=1-flag;
                        ref=i+K-1;
                        if(ref<ele){
                            range.add(j+1,ele);
                            ele=ref;
                            ref2+=1;
                        }
                        else{
                            if(ref>ele){
                                range.add(j+ref2,ref);
                                ref2+=1;
                            }
                        }
                    }
                }
            }
            i++;
        }
        
        return ans;
    }