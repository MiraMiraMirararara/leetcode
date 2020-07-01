from typing import List 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.idx=0
 
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int,idx:int) -> TreeNode:
        if not root:#首次插入元素
            root=TreeNode(val)
            root.idx=idx
            return root
        if root.val<val:#插入元素比当前元素大，插入至右子树
            root.right=self.insertIntoBST(root.right,val,idx)  
        else:#插入元素比当前元素小或等于，插入至左子树
            root.left=self.insertIntoBST(root.left,val,idx) 
        return root
    def searchBST(self, root: TreeNode, val: int,t:int,idx:int) -> TreeNode:
        if not root: #根节点为空或未找到
            return False
        if root.val<val-t:#小于满足条件最小值，在右子树中继续找
            return self.searchBST(root.right,val,t,idx)  
        elif root.val>val+t:#大于满足条件最大值，在左子树中继续找
            return self.searchBST(root.left,val,t,idx) 
        else:
            if root.idx!=idx:#该节点并非插入节点
                return True #满足条件
            else:return False
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
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        root=None
        for i in range(len(nums)):
            if i>k:
                #删除第nums[i-k]，即删除最先插入的元素
                root=self.deleteNode(root,nums[i-k-1])
            #插入并查询
            root=self.insertIntoBST(root,nums[i],i)
            if i>0:
                if self.searchBST(root,nums[i],t,i):
                    return True
        return False
sl=Solution()
print(sl.containsNearbyAlmostDuplicate([1,5,9,1,5,9]
,2
,3))