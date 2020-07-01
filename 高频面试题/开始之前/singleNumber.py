from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res^=i
        return res
sl=Solution() 
print(sl.singleNumber([1,1,2]))