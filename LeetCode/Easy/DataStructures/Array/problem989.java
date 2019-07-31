class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
        LinkedList<Integer> ans = new LinkedList<Integer>();
        int digit,sum;int a;
        int i=A.length-1;
        int carry=0;
        while(K!=0 || i>=0){
            digit=K%10;
            K/=10;
            if(i>=0)a=A[i];
            else a=0;
            sum=a+digit+carry;
            if(sum>9){
                carry=1;
                sum%=10;
            }
            else{
                carry=0;
            }
            ans.addFirst(sum);
            i--;
        }
        if(carry==1)ans.addFirst(1);
        return ans;
    }
}