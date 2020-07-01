from typing import List 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_cp=nums1[:m]
        i,j,k=0,0,0
        while i<m and j<n:
            if nums1_cp[i]<nums2[j]:
                nums1[k]=nums1_cp[i] 
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        if  i<m:
            nums1[k:]=nums1_cp[i:] 
        if  j<n:
            nums1[k:]=nums2[j:] 
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k,i,j=m+n-1,m-1,n-1
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[k]=nums2[j] 
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        if  i>=0:
            nums1[:k+1]=nums1[:i+1] 
        if  j>=0:
            nums1[:k+1]=nums2[:j+1] 