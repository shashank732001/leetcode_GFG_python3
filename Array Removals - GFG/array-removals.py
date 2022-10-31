#User function Template for python3


class Solution:

	def removals(self,arr, n, k):
		# code here
		i = 0
		j = i+1
		ans = n-1
		arr.sort()
		
		while i<n-1:
		    if i==j:
		        j+=1
		    while j<n and arr[j]-arr[i]<=k:
		      #  print(arr[j],arr[i])
		        ans = min(ans,n-(j-i+1))
		        j+=1
		    i+=1
		  #  j+=1
		return ans    
		        
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends