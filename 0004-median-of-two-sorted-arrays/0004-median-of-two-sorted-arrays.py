class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lsts = sorted(nums1+nums2)
        
        if len(lsts)%2 == 0:
	        a = len(lsts)//2
	
	        return (lsts[a-1]+lsts[a])/2
        else:
	        a = len(lsts)//2
	        return lsts[a]