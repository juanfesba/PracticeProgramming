class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        DP={}
        
        def phi(availWidth,lastHeigth,i):
            nonlocal DP
            check=DP.get((availWidth,lastHeigth,i))
            if check!=None:
                return check
            if i==len(books):
                return 0
            if availWidth==0:
                availWidth=shelf_width
                lastHeigth=0
            heigth=books[i][1]
            width=books[i][0]
            if availWidth==shelf_width:
                ans=heigth+phi(shelf_width-width,heigth,i+1)
            else:
                opt1=heigth+phi(shelf_width-width,heigth,i+1)
                opt2=float("inf")
                if availWidth>=width:
                    opt2=0
                    diff=heigth-lastHeigth
                    if diff>0:
                        opt2+=diff
                        lastHeigth=heigth
                    opt2+=phi(availWidth-width,lastHeigth,i+1)
                ans=min(opt1,opt2)
                
            DP[(availWidth,lastHeigth,i)]=ans
            return ans
        
        return phi(shelf_width,0,0)
