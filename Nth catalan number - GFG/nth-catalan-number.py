#User function Template for python3

class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        #return the nth Catalan number.
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            count = 0
            
            for j in range(1,n+1):
                
                count += dp[j-1]*dp[i-j]
            
            dp[i]=count
        return dp[-1]    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends