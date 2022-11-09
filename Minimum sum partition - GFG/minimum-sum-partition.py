#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		def isSubsetSum (N, arr, sum):
        
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
            
            return dp[-1]
            
        v = isSubsetSum(n,arr,sum(arr))
        # ans = [i for i in range(len(v))]
        # print(v)
        Sum = sum(arr)
        Min = 10e9
        for i in range((len(v)//2)+1):
            if v[i]==True and (Sum-2*i)>=0:
                Min = min(Min,Sum-2*i) 
        return Min        
                
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends