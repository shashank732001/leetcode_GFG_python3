#User function Template for python3

class Solution:
	def AlternatingaMaxLength(self, nums):
		# Code here
		inc=1
		dec=1
		
		for i in range(1,len(nums)):
		    if nums[i]>nums[i-1]:
		        inc=dec+1
		    elif nums[i]<nums[i-1]:
		        dec = inc+1
		return max(inc,dec)        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.AlternatingaMaxLength(nums)
		print(ans)

# } Driver Code Ends