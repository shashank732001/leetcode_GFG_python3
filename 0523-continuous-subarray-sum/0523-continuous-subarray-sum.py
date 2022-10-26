class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        start = 0
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1] == 0):
                return True
        d = defaultdict(int)
        d[0] = 1
        for i in nums:
            start = (start + i) % k
            if(i and start in d and (d[start] >= 2 or i%k)):
                return True
            d[start] += 1
        return False