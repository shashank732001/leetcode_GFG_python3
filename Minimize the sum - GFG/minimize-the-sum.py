#User function Template for python3
import heapq

class Solution:
    def minimizeSum(self, N, arr):
        # Code here
        heapq.heapify(arr)
        ans = 0
        while len(arr)>1:
            fir = heapq.heappop(arr)
            sec = heapq.heappop(arr)
            ans += fir+sec
            heapq.heappush(arr,fir+sec)
        return ans    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends