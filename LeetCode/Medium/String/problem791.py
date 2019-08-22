class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans=""
        dic=collections.defaultdict(int)
        lettersT=set()
        lettersS=set(S)
        for char in T:
            dic[char]+=1
            lettersT.add(char)
        lettersT-=lettersS
        for cord in S:
            adding=cord*dic[cord]
            ans+=adding
        for e in lettersT:
            adding=e*dic[e]
            ans+=adding
        return ans
