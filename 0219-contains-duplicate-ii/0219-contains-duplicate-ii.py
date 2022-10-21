class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==k: return len(set(nums))<len(nums)
        if len(set(nums))==len(nums): return False   # if no duplicates exist return false

        for i in range(len(nums)-k+2):  # sliding window of size k over nums
            subarr = nums[i:i+k+1]
            if len(set(subarr))<len(subarr):  # check if subarray has duplicates
                return True
        return False      
