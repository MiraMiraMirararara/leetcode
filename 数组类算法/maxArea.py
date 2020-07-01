from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        ans=0
        while i<j: 
            tmp=(j-i)*min(height[i],height[j])
            ans=max(tmp,ans)
            if height[i]>height[j]: j-=1
            else: i+=1
        return ans 
sl=Solution() 
print(sl.maxArea([1,8,6,2,5,4,8,3,7]))