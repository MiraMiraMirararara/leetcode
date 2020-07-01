from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countDict={}
        for i in nums:
            if i not in countDict:
                countDict[i]=1
            else:countDict[i]+=1
        res=sorted(countDict.items(),key=lambda x: x[1],reverse=True)
        return res[0][0]
sl=Solution() 
print(sl.majorityElement([3,2,3]))