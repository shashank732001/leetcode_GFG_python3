#User function Template for python3

class Solution:
    def maxSquare(self, n, m, mat):
        # code here
        
        
        # def square(i,j,ans):
            
        #     if i not in range(n) or j not in range(m):
        #         return 0
             
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
              
        #     right = square(i,j+1,ans)
        #     diag = square(i+1,j+1,ans)
        #     down = square(i+1,j,ans)
            
        #     if mat[i][j]==1:
        #         dp[i][j] = min(right,diag,down)+1
                
        #         ans[0]=max(ans[0],dp[i][j])
        #         return dp[i][j]
    
        #     else:
        #         dp[i][j] = 0
        #         return dp[i][j]
        
        
        # dp = [[-1]*m for i in range(n)]
        # ans = [0]
        # square(0,0,ans)
        # return ans[0]
        
        dp = [[0]*(m+1) for i in range(n+1)]
        ans = 0
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                
                right = dp[i][j+1]
                diag = dp[i+1][j+1]
                down = dp[i+1][j]
                
                if mat[i][j]==1:
                    dp[i][j]= min(right,diag,down)+1
                    ans = max(ans,dp[i][j])
                else:
                    dp[i][j]=0
                
        return ans        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        arr = input().split()
        for i in range(n*m):
            mat[i//m][i%m] = int(arr[i])
        
        ob = Solution()
        print(ob.maxSquare(n, m, mat))
# } Driver Code Ends