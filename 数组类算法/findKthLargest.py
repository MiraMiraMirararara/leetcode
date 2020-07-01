from typing import List 
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
def partition(nums,left,right):
        pivot=left
        index=pivot+1 #控制最大值
        i=index#控制最小值
        while i<=right:
            if nums[i]<nums[pivot]:
                swap(nums,i,index)
                index+=1
            i+=1
        swap(nums,pivot,index-1)
        return index-1
def select(nums, k_smallest):
    if len(nums)==1:return nums[0]
    pivot=partition(nums,0,len(nums)-1) 
    if pivot==k_smallest:
        return nums[pivot]
    elif pivot<k_smallest: 
        return select(nums[pivot+1:],k_smallest-pivot-1)
    else:
        return select(nums[:pivot],k_smallest) 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return select(nums,len(nums)-k)
sl =Solution()
print(sl.findKthLargest([3,2,3,1,2,4,5,5,6],4))