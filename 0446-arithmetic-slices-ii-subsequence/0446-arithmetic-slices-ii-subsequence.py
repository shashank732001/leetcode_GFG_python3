class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        res = 0
        
        #ending index
        for i in range(n):
            #starting index
            for j in range(i):
                
                diff = nums[i]-nums[j]
                dp[i][diff] += (1+dp[j][diff])
                res += dp[j][diff]
        return res        