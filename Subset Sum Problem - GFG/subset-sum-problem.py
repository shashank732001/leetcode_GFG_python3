#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp = [["."]*(sum+1) for i in range(N+1)]
        
        
        for i in range(N+1):
            for j in range(sum+1):
                
                if i==0:
                    dp[i][j]=False
                
                if j==0:
                    dp[i][j]=True
                
                if i==0 and j==0:
                    dp[i][j]=True
        # print(dp)
        
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends