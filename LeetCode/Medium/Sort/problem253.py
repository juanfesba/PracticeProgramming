class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ranges=[]
        i=0
        ans=0
        for interval in intervals:
            while(i!=len(ranges) and interval[0]>=ranges[i][1]):i+=1
            
            j=i
            flag=True
            
            while flag and j!=len(ranges):
                if interval[1]>ranges[j][1]:
                    ranges[j][2]+=1
                    ans=max(ans,ranges[j][2])
                    interval[0]=ranges[j][1]
                    j+=1
                else:
                    if interval[1]<ranges[j][1]:
                        ranges[j][0]=interval[1]
                        tmp=ranges[j][2]+1
                        ranges.insert(j,[interval[0],interval[1],ranges[j][2]+1])
                        ans=max(ans,tmp)
                    else:
                        ranges[j][2]+=1
                        ans=max(ans,ranges[j][2])
                    flag=False
                    
                    
            if j==len(ranges):
                ranges.append([interval[0],interval[1],1])
                ans=max(ans,ranges[j][2])
        
        
        return ans
