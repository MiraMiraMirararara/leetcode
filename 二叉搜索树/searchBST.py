class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:return root
        if root.val==val:return root
        elif root.val<val:return self.searchBST(root.right,val)
        else:return self.searchBST(root.left,val)
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

sl=Solution()
res=sl.searchBST(root,5)
if res: print(res.val)
else:print("None")