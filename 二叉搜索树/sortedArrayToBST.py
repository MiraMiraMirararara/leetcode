from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self,nums: List[int],low,high)->TreeNode:
        if low==high:return None
        rootIdx=(high+low)//2 #如果是奇数，向下取整实则为中位左边一位
        root=TreeNode(nums[rootIdx])#创建根节点
        root.left=self.helper(nums,low,rootIdx)#递归连接左子树
        root.right=self.helper(nums,rootIdx+1,high)#递归连接右子树
        return root
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode: 
        if not nums:return None
        return self.helper(nums,0,len(nums)) 