class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def helper(self,cur,low=float('-inf'),high=float('inf')):
        if not cur:return True
        val=cur.val
        if val<=low or val>=high:return False
        return self.helper(cur.left,low,val) and  self.helper(cur.right,val,high)
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root)
 
       
root=TreeNode(5)
left=TreeNode(6)
right=TreeNode(7)
root.left=left
root.right=right
sl=Solution()
sl.isValidBST(root)