#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        n = N
        dp = [["." for i in range(W+1)] for j in range(n+1)]  #we taking "." as initial value ,we can consider anything
        
        # initializing the value at n=0 or w=0,
        #we are considering 0 beacuse it was our return value in base condition
        for i in range(n+1):
            for j in range(W+1):
                if i==0 or j==0:
                    dp[i][j]=0
                    
        # now we fill the matrix solving all subproblems
        # this is nothing but our choice tree
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(val[i-1]+dp[i][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
                    
        return dp[n][W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends