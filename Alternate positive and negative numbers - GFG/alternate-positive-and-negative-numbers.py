#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        pos = [num for num in arr if num>=0]
        neg = [num for num in arr if num<0]
        
        # print(pos)
        # print(neg)
        i = 0
        while pos or neg:
            if pos:
                arr[i]=pos.pop(0)
                i+=1
                # print(res)
            if neg:
                arr[i]=neg.pop(0)
                i+=1
                # print(res)
         
        
        return arr      
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends