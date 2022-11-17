class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,string):
        # Code here
        
        def subs(i,j,strg):
            
            if i>j:
                return 0
                
            if i==j:
                return 1
                
            if dp[i][j]!=-1:
                return dp[i][j]
                
            if strg[i]==strg[j]:
                dp[i][j] = subs(i+1,j,strg)+subs(i,j-1,strg)+1
                
            else:
                dp[i][j] = subs(i+1,j,strg)+subs(i,j-1,strg)-subs(i+1,j-1,strg)
                
            return dp[i][j]    
        
        n = len(string)
        MOD = 10**9+7
        dp = [[-1]*(n) for i in range(n)]
        ans = subs(0,n-1,string)
        return ans%MOD
        

#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends