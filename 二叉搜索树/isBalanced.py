class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#自顶向下
class Solution:
    def height(self,root:TreeNode):
        if not root:return -1
        return 1+max(self.height(root.left),self.height(root.right))
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:return True
        return abs(self.height(root.left)-self.height(root.right))<2 and self.isBalanced(root.right) and self.isBalanced(root.left)
#自底向下
class Solution2:
    def helper(self,root:TreeNode)->(bool,int):
        if not root:return True,-1
        leftBalance,leftHeight=self.helper(root.left)
        if not leftBalance:return False,0
        rightBalance,rightHeight=self.helper(root.right)
        if not rightBalance:return False,0 
        return abs(leftHeight-rightHeight)<2 ,1+max(rightHeight,leftHeight)
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)[0]
