class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root=TreeNode(val)
            return root
        if root.val<val:
            root.right=self.insertIntoBST(root.right,val) 
        elif root.val>val:
            root.left=self.insertIntoBST(root.left,val)
        return root

root=TreeNode(6)
left=TreeNode(4)
right=TreeNode(10)
left1=TreeNode(2)
right1=TreeNode(5)
left2=TreeNode(8)
right2=TreeNode(12)
left.left=left1
left.right=right1
right.left=left2
right.right=right2
root.left=left
root.right=right        