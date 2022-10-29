#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        smallest = 10e9
        largest = -10e9
        arr.sort()
        diff = arr[-1]-arr[0]
        
        for i in range(1,n):
            # if arr[i]-k<0:continue
            smallest = min(arr[0]+k,arr[i]-k)
            largest = max(arr[-1]-k,arr[i-1]+k)
            diff = min(diff,largest-smallest)
        return diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends