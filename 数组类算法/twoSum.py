from typing import List 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictData={}
        res=[]
        for i in range(len(numbers)):
            if target-numbers[i] in dictData and i+1!=dictData[target-numbers[i]]:
                res.append(min(i+1,dictData[target-numbers[i]]))
                res.append(max(i+1,dictData[target-numbers[i]]))
                return res
            dictData[numbers[i]]=i+1
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while i<j:
            tmp=numbers[i]+numbers[j]
            if target==tmp:
                return [i+1,j+1]
            elif target<tmp:
                j-=1
            else:i+=1
        
        
sl=Solution()
print(sl.twoSum2([0,0,3,4],0))