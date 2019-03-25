import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.equals("")){
            return 0;
        }
        HashMap <Character,Integer> hm=new HashMap<Character,Integer>();
        int i=0;
        char current,previous;
        int ans=1;
        int aux=0;
        while (i<s.length()){
            current=s.charAt(i);
            if(hm.containsKey(current)){
                previous=s.charAt(i-1);
                if(previous==current){
                    aux=1;
                }
                else{
                    aux=Math.min(aux+1,i-hm.get(current));
                }
                ans=Math.max(aux,ans);
            }
            else{
                aux+=1;
                ans=Math.max(aux,ans);
            }
            hm.put(current,i);
            i++;
        }
        return ans;
    }
}