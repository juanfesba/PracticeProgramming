# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        high=mountain_arr.length()
        best=high
        flag=0
        
        def binsearch(low,hi):
            nonlocal best,flag
            if flag==3:
                return
            if low+1==hi:
                if mountain_arr.get(low)==target:
                    best=min(best,low)
                    flag=3   
                return
            if low==high-2:
                if mountain_arr.get(low)==target:
                    best=min(best,low)
                    flag=3
                if mountain_arr.get(low+1)==target:
                    best=min(best,low+1)
                    flag=3
                return
            #flag = 0:dont know 2:right 3:end
            mid=low+((hi-low)>>1)
            check=mountain_arr.get(mid)
            check1=mountain_arr.get(mid-1)
            check2=mountain_arr.get(mid+1)
            
            if check1<check>check2:
                #case peak
                if check==target:
                    best=mid
                    return
                else:
                    binsearch(low,mid)
                    binsearch(mid,hi)
            elif check1<check<check2:
                #case left
                if check==target:
                    best=mid
                    flag=3
                    return
                else:
                    if check>target:
                        binsearch(low,mid)
                    binsearch(mid,hi)
            elif check1>check>check2:
                #case right
                if check==target:
                    flag=2
                    best=mid
                    binsearch(low,mid)
                else:
                    if flag==2:
                        binsearch(low,mid)
                    else:
                        if check>target:
                            binsearch(low,mid)
                            binsearch(mid,hi)
                        else:
                            binsearch(low,mid)
                
        binsearch(0,high)
        if best==high:
            best=-1
        return best
