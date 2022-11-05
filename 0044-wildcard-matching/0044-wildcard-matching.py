class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [["."]*(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                
                if i==0 and j==0:
                    dp[i][j]=True
                
                if j==0 and i>0:
                    dp[i][j]=False
                
                if i==0 and j>0:
                    if p[j-1] =="*":
                        dp[i][j]=dp[i][j-1]
                        
                    else:
                        dp[i][j]= False
                        
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if s[i-1]==p[j-1] or p[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                    
                elif p[j-1]=="*":
                    dp[i][j] = ( dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1])
                    
                else:
                    dp[i][j]=False
                
        return dp[-1][-1]        
        # print(dp)                
                        