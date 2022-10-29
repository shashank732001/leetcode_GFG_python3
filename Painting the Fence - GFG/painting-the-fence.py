#User function Template for python3

class Solution:
    def countWays(self,n,k):
        mod = (10**9)+7
        #code here.
        def add(a,b):
            return ((a%mod)+(b%mod))%mod
            
        def mul(a,b):
            return ((a%mod) * (b%mod))%mod
        
        
        
        """
        Recursive approach
        """
        # def solveRec(n,k):
            
        #     if n==1:
        #         return k
        #     if n==2:
        #         return add(k,mul(k,k-1))
                
        #     ans = add(mul(solveRec(n-2,k),k-1),mul(solveRec(n-1,k),k-1))  
            
        #     return ans
        
        # return solveRec(n,k)    
        
        
        """
        Memoization
        """
        # def solveMem(n,k,dp):
            
        #     if n==1:
        #         return k
        #     if n==2:
        #         return add(k,mul(k,k-1))
        #     if dp[n]!=-1:
        #         return dp[n]
                
        #     dp[n] = add(mul(solveMem(n-2,k,dp),k-1),mul(solveMem(n-1,k,dp),k-1))  
            
        #     return dp[n]
        # dp = [-1]*(n+1) 
        # return solveMem(n,k,dp)
        
        
        """
        top-down approach
        """
        
        dp = [0]*(n+1)
        if n==1:return k
        dp[1] = k
        dp[2] = add(k,mul(k,k-1))
        
        for i in range(3,n+1):
            
            dp[i] = add(mul(dp[i-2],k-1),mul(dp[i-1],k-1))
            # print(add(mul(dp[i-2],k-1),mul(dp[i-1],k-1)))
        # print(dp)
        
        return dp[-1]    



#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends