#User function Template for python3
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        # heapq.heapify(arr)
        # while k>0:
        #     res = heapq.heappop(arr)
        #     k-=1
        # return res    
        # return sorted(arr)[k-1]
        
        arr1 = []
        heapq.heapify(arr1)
        for i in arr:
            heapq.heappush(arr1,i)
        # res = arr[0]    
        while k>0:
            ele = heapq.heappop(arr1)
            
            k-=1
        return ele    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends