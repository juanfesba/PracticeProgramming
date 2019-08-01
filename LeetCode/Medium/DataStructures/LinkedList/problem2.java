/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans=new ListNode(0);
        ListNode tempans=ans;
        int carry=0,i=1;
        int maxi=Math.max(length(l1),length(l2));
        while(i<=maxi){
            if (l1!=null){
                tempans.val+=l1.val;
                l1=l1.next;
            }
            if(l2!=null){
                tempans.val+=l2.val;
                l2=l2.next;
            }
            tempans.val+=carry;
            if (tempans.val>9){
                carry=1;
                tempans.val%=10;
            }
            else{
                carry=0;
            }
            if(i==maxi){
                if (carry==1){
                    tempans.next=new ListNode(1);
                }
                else{
                    break;
                }
            }
            else{
                tempans.next=new ListNode(0);
                tempans=tempans.next;
            }
            i+=1;
        }
        return ans;
    }
    public int length(ListNode l){
        ListNode temp=l;
        int i=0;
        while (temp!=null){
            i+=1;
            temp=temp.next;
        }
        return i;
    }
}