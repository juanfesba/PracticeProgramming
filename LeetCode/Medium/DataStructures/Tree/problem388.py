class Solution:
    def lengthLongestPath(self, input: str) -> int:
        best=0
        acc=0
        count=0
        stack=[0]
        level=0
        tipo=False
        i=0
        while(i<len(input)):
            char=input[i]
            
            if char==".":
                count+=1
                tipo=True
            elif char=="\n":
                if tipo:
                    stack=stack[:level+1]
                    acc=stack[-1]
                    acc+=count
                    
                    
                    best=max(best,acc) ##
                    count=0
                    level=0
                    tipo=False
                    ############
                else:
                    stack=stack[:level+1]
                    acc=stack[-1]
                    acc+=count+1
                    stack.append(acc)
                    count=0
                    level=0
            elif char=="\t":
                level+=1
            else:
                count+=1
            
            i+=1
        if tipo:
            stack=stack[:level+1]
            acc=stack[-1]
            acc+=count
            best=max(best,acc)
            
        
        return best
