class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        offset=0
        left=0
        for char in S:
            if char==")":
                if left==0:
                    offset+=1
                else:
                    left-=1
            else:
                left+=1
        return offset + left
        
