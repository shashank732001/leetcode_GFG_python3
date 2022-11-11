class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0 
        r = 1
        if n==1 : return n
        while r<n:
            if nums[l]!=nums[r]:
                l+=1
                nums[l]=nums[r]
            r+=1
        return l+1    
                