class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: 
    def findLeft(self,cur: TreeNode): 
        while cur.left: 
            cur=cur.left
        return cur.val
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:return root
        if root.val==key: 
            if root.right and root.left:#有两个子节点
                root.val=self.findLeft(root.right)#找到右子树的最小值 
                root.right=self.deleteNode(root.right,root.val)
            elif root.right:
                root=root.right
            elif root.left:
                root=root.left
            else :root=None  
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            root.left=self.deleteNode(root.left,key)
        return root
root=TreeNode(5)
left=TreeNode(3)
right=TreeNode(6)
left1=TreeNode(2)
right1=TreeNode(4) 
right2=TreeNode(7)
left.left=left1
left.right=right1 
right.right=right2
root.left=left
root.right=right
sl=Solution()
root=sl.deleteNode(root,3)
print(root.val)