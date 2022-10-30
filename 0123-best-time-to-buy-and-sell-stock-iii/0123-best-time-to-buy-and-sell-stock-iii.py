class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n
        k = 2
        
        if k>n:
            A = [prices[i]-prices[i-1] for i in range(1,n)]
            return sum([b for b in A if b>0])
        
        for tns in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(1,n):
                pos = max(pos,dp[i]-prices[i])
                profit = max(profit,pos+prices[i])
                dp[i] = profit
        return dp[-1]