class Solution:
    def candy(self, arr: List[int]) -> int:
        for e in range(len(arr)):
            if e==0:
                ans=1
                peek=1
                last=1
                acc=0
            else:
                if(arr[e]>arr[e-1]):
                    last+=1
                    peek=last
                    ans+=last
                    acc=0
                elif(arr[e]==arr[e-1]):
                    peek=1
                    acc=0
                    last=1
                    ans+=1
                else:
                    last=1
                    acc+=1
                    if(acc==peek):
                        peek+=1
                        ans+=1
                    ans+=acc
        return int(ans)
