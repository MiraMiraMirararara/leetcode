class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack=[]
        self.findLeft(root)
    def findLeft(self,cur: TreeNode): 
        while cur:
            self.stack.append(cur)
            cur=cur.left 
    def next(self) -> int:
        """
        @return the next smallest number
        """ 
        minNode= self.stack.pop()
        if minNode.right:#右节点不为空
            self.findLeft(minNode.right)
        return minNode.val
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0
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
sl=BSTIterator(root)
while sl.hasNext():
     print(sl.next())