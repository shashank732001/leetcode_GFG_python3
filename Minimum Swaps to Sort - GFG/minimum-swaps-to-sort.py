

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		lookup = {}
		n = len(nums)
		arr = nums.copy()
		arr.sort()
		count = 0
		
		for i in range(n):
		    lookup[nums[i]]=i
		
		for i in range(n):
		    if nums[i]==arr[i]:
		        continue
		    idx = lookup[arr[i]]
		    lookup[nums[i]]=idx
		    lookup[nums[idx]]=i
		    nums[i],nums[idx]=nums[idx],nums[i]
		    count+=1
		return count    

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends