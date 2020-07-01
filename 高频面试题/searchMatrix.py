class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:return False
        i,j=len(matrix)-1,0 
        while i>=0 and j<len(matrix[0]):
            cur=matrix[i][j]
            if cur==target:return True
            elif cur<target:j+=1
            else:i-=1
        return False
sl=Solution() 
print(sl.searchMatrix([[-1,3]],3))
        