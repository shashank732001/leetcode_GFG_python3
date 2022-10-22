#User function Template for python3

class Solution:
    def fillingBucket(self, N):
        # code here
        def helper(dp,n):
            
            if n==1:
                return 1
                
            if n==2:
                return 2
            
            
            dp[0] = 1
            dp[1] = 2
            for i in range(2,n):
                dp[i]= (dp[i-1]+dp[i-2])%100000000
                
            return dp[n-1]    
        
        
        
        dp = [-1]*N
        return helper(dp,N)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.fillingBucket(N))
# } Driver Code Ends