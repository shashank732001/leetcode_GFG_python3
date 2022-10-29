#User function Template for python3
class Solution:
	def minCoins(self, coins, M, V):
		# code here
		
		dp = [["."]*(V+1) for i in range(M+1)]
		
		for i in range(M+1):
		    for j in range(V+1):
		        
		        if j == 0:
		            dp[i][j]=0
		        if i ==0:
		            dp[i][j]=float("infinity")-1
		            
		for j in range(1,V+1):
		    i=1
		    
		    if j%coins[0]==0:
		        dp[i][j]=j//coins[0]
		    else:
		        dp[i][j]=float("infinity")-1
		
		for i in range(2,M+1):
		    for j in range(1,V+1):
		        
		        if coins[i-1]<=j:
		            dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
		        else:
		            dp[i][j]=dp[i-1][j]
		            
		return dp[-1][-1] if dp[-1][-1]<=V else-1           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends