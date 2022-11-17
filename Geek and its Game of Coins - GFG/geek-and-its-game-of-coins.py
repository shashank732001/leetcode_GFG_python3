#User function Template for python3
class Solution:
	def findWinner(self, N,X,Y):
		# code here
		dp = [0]*(N+1)
		dp[1]=1
		
		for i in range(2,N+1):
		    
		    if i-1>=0 and not dp[i-1]:
		        dp[i]=1
		        
		    elif i-X>=0 and not dp[i-X]:
		        dp[i]=1  
		        
		    elif i-Y>=0 and not dp[i-Y]:
		        dp[i]=1
	    
	    return dp[-1]	        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,X,Y = input().split()
		N,X,Y = int(N),int(X),int(Y)
		ob = Solution()
		ans = ob.findWinner(N,X,Y)
		print(ans)

# } Driver Code Ends