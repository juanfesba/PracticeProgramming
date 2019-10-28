class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        count = 0
        index= 0
        
        realpattern={}
        
        for char in pattern:
            check = realpattern.get(char)
            if check!=None:
                realpattern[index]=check
            else:
                realpattern[char]=count
                realpattern[index]=count
                count+=1
                
            index += 1
        
        ans = []
        for word in words:
            wordpattern={}
            count = 0
            index= 0
            flag=False
            
            for char in word:
                check = wordpattern.get(char)
                if check==None:
                    wordpattern[char]=count
                    check=count
                    count+=1
                if check != realpattern[index]:
                    flag=True
                if flag:
                    break
                    
                index+=1
                
            if not(flag):
                ans.append(word)
            
        return ans
