class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        start = 0
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1] == 0):
                return 1
        d = defaultdict(int)
        d[0] = 1
        for i in nums:
            start = (start + i) % k
            if(i and start in d and (d[start] >= 2 or i%k)):
                return 1
            d[start] += 1
        return 0