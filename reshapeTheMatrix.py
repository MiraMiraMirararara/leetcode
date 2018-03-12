class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp=[]
        m=len(nums)
        n=len(nums[0])
        if m*n==r*c:
            res=[([0]*c)for i in range(r)]
            for _,row in enumerate(nums):
                for _,element in enumerate(row):
                    temp.append(element)
            index =0
            for i in range(r):
                for j in range(c):
                    res[i][j]=temp[index]
                    index+=1
            return res
        else:
            return nums