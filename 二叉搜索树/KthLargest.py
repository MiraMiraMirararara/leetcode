from typing import List 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count=1
# class KthLargest:
#     def insertIntoBST(self, cur: TreeNode, val: int) -> TreeNode:
#         if not cur:#首次插入元素
#             cur=TreeNode(val)
#             return cur
#         if cur.val<val:#插入元素比当前元素大，插入至右子树
#             cur.right=self.insertIntoBST(cur.right,val)  
#         else:#插入元素比当前元素小或等于，插入至左子树
#             cur.left=self.insertIntoBST(cur.left,val)
#         cur.count+=1#若插入至子树，当前节点的count需要+1
#         return cur
#     def __init__(self, k: int, nums: List[int]):
#         self.root=None 
#         self.k=k
#         for i in nums:#逐个插入
#             self.root=self.insertIntoBST(self.root,i) 
#     def findKHelper(self,cur:TreeNode,k)->TreeNode:
#         curCnt=1#如果无右节点，当前是第1大的数
#         if cur.right:#如果有右节点，则当前是cur.right.count+1大的数
#             curCnt+=cur.right.count
#         if k==curCnt:#当前值即为第k大
#             return cur
#         elif k<curCnt:#第k大在右子树
#             return self.findKHelper(cur.right,k)
#         else:#第k大在左子树，为左子树的第k-curCnt大
#             return self.findKHelper(cur.left,k-curCnt)
#     def add(self, val: int) -> int:
#         self.root=self.insertIntoBST(self.root,val)
#         return self.findKHelper(self.root,self.k).val
# class KthLargest:
#     def insertIntoBST(self, cur: TreeNode, val: int) -> TreeNode:
#         if not cur:#首次插入元素
#             cur=TreeNode(val)
#             return cur
#         if cur.val<val:#插入元素比当前元素大，插入至右子树
#             cur.right=self.insertIntoBST(cur.right,val)  
#         else:#插入元素比当前元素小或等于，插入至左子树
#             cur.left=self.insertIntoBST(cur.left,val)
#         cur.count+=1#若插入至子树，当前节点的count需要+1
#         return cur 
#     def __init__(self, k: int, nums: List[int]):
#         self.root=None 
#         self.k=k
#         self.kLarge=None#记录第k大
#         for i in nums:#逐个插入
#             self.root=self.insertIntoBST(self.root,i) 
#     def findKHelper(self,cur:TreeNode,k)->TreeNode:
#         curCnt=1#如果无右节点，当前是第1大的数
#         if cur.right:#如果有右节点，则当前是cur.right.count+1大的数
#             curCnt+=cur.right.count
#         if k==curCnt:#当前值即为第k大
#             return cur
#         elif k<curCnt:#第k大在右子树
#             return self.findKHelper(cur.right,k)
#         else:#第k大在左子树，为左子树的第k-curCnt大
#             return self.findKHelper(cur.left,k-curCnt)
#     def add(self, val: int) -> int:
#         #self.kLarge没有值，或者当前值大于self.kLarge才插入
#         if self.kLarge and val>self.kLarge or not self.kLarge:
#             self.root=self.insertIntoBST(self.root,val)
#         self.kLarge=self.findKHelper(self.root,self.k).val
#         return self.kLarge
class KthLargest:
    def insertIntoBST(self, cur: TreeNode, val: int) -> TreeNode:
        if not cur:#首次插入元素
            cur=TreeNode(val)
            return cur
        if cur.val<val:#插入元素比当前元素大，插入至右子树
            cur.right=self.insertIntoBST(cur.right,val)  
        else:#插入元素比当前元素小或等于，插入至左子树
            cur.left=self.insertIntoBST(cur.left,val)
        cur.count+=1#若插入至子树，当前节点的count需要+1
        return cur 
    def __init__(self, k: int, nums: List[int]):
        self.root=None 
        self.k=k
        self.kLarge=None#记录第k大
        for i in nums: 
            #若根节点为空，或者根节点的count<k直接插入
            if not self.root or self.root.count<k :
                self.root=self.insertIntoBST(self.root,i)  
            else:#当前二叉搜索树的元素数>=k
                if not self.kLarge:#计算第k大
                    self.kLarge=self.findKHelper(self.root,k).val
                if i>self.kLarge:#如果当前值大于第k大，插入并重新寻找第k大
                    self.root=self.insertIntoBST(self.root,i) 
                    self.kLarge=self.findKHelper(self.root,k).val

    def findKHelper(self,cur:TreeNode,k)->TreeNode:
        curCnt=1#如果无右节点，当前是第1大的数
        if cur.right:#如果有右节点，则当前是cur.right.count+1大的数
            curCnt+=cur.right.count
        if k==curCnt:#当前值即为第k大
            return cur
        elif k<curCnt:#第k大在右子树
            return self.findKHelper(cur.right,k)
        else:#第k大在左子树，为左子树的第k-curCnt大
            return self.findKHelper(cur.left,k-curCnt)
    def add(self, val: int) -> int:
        #self.kLarge没有值，或者当前值大于self.kLarge才插入
        if self.kLarge and val>self.kLarge or not self.kLarge:
            self.root=self.insertIntoBST(self.root,val)
        self.kLarge=self.findKHelper(self.root,self.k).val
        return self.kLarge
k=KthLargest(3,[4,5,8,2])
print(k.add(3))
print(k.add(5))
print(k.add(10))
print(k.add(9))
print(k.add(4))
