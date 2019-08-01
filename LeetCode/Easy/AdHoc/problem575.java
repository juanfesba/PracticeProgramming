class Solution {
    public int distributeCandies(int[] candies) {
        HashMap<Integer,Boolean>kinds=new HashMap<Integer,Boolean>();
        int ans;
        int cand=0;
        int stock=0;
        for(int i=0;i<candies.length;i++){
            if(kinds.get(candies[i])==null){
                cand+=1;
                kinds.put(candies[i],true);
            }
            else stock+=1;
        }
        if(stock>cand)ans=cand;
        else ans=stock+(cand-stock)/2;
        return ans;
    }
}