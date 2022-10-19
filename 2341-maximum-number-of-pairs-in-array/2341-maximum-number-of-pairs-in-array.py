class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        i = 0
        count=0
        while i<len(nums):
            nums1 = nums[i]
            if nums1 in nums[i+1:]:
                nums.remove(nums1)
                nums.remove(nums1)
                count+=1
            else:
                i+=1
        return [count,len(nums)]        
                
                
            