from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i,j=0,0
        minLen=float('inf')
        curSum=0
        while j<len(nums):
            curSum+=nums[j]
            while curSum>=s:
                minLen=min(minLen,j-i+1)
                curSum-=nums[i]
                i+=1
            j+=1
        return minLen if minLen!=float('inf') else 0

sl=Solution() 
print(sl.minSubArrayLen(3,[1,1]))