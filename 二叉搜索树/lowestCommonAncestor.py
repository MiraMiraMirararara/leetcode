class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return root
        minV=min(p.val,q.val)
        maxV=max(p.val,q.val)
        if minV<=root.val<=maxV:return root
        if root.val<minV:return self.lowestCommonAncestor(root.right,p,q)
        if root.val>maxV:return self.lowestCommonAncestor(root.left,p,q)