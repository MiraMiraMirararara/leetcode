class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum=0
        temp=0
        for num in nums:
            if num==1:
                temp+=1
                if temp>maxnum:
                    maxnum=temp
            else:
                temp=0     
        return maxnum