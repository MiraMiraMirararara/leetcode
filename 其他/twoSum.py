class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexs=[]
        state=0
        for index in range(len(nums)):
            base=nums[index]
            for j in range(index+1,len(nums)):
                if base+nums[j]==target:
                    indexs.append(index)
                    indexs.append(j)
                    state=1
                    break
            if state==1 :break
        return indexs
