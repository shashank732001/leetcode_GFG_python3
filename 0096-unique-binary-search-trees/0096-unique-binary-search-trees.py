class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        
        for i in range(2,n+1):
            Sum=0
            for j in range(1,i+1):
                
                leftBST = dp[j-1]
                rightBST  = dp[i-j]
                
                Sum += leftBST*rightBST
            dp[i]=Sum 
        return dp[-1]    