class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        best=1
        ans=s[0]
        for i in range(len(s)*2-1):
            if i%2==0:
                cur=1
                index=i>>1
                left=index-1
                right=index+1
                while(left>=0 and right<len(s)):
                    if s[left]==s[right]:
                        cur+=2
                        if cur>best:
                            best=cur
                            ans=s[left:right+1]
                    else:
                        break
                    left-=1
                    right+=1
            else:
                cur=0
                left=(i-1)>>1
                right=left+1
                while(left>=0 and right<len(s)):
                    if s[left]==s[right]:
                        cur+=2
                        if cur>best:
                            best=cur
                            ans=s[left:right+1]
                    else:
                        break
                    left-=1
                    right+=1
        return ans
