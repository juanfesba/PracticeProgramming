class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        frecDic=collections.defaultdict(int)
        for char in tiles:
            frecDic[char]+=1
        
        lenT=len(tiles)
        if lenT==1:
            return len(frecDic)
        
        ans=0
        def combinatory(deep):
            nonlocal ans
            nonlocal frecDic
            if deep==lenT+1:return
            
            for key in frecDic.keys():
                if frecDic[key]>0:
                    frecDic[key]-=1
                    ans+=1
                    combinatory(deep+1)
                    frecDic[key]+=1
            
        combinatory(1)
        return ans
