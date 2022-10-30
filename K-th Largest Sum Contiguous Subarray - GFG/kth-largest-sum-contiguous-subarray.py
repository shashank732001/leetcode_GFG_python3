from typing import List


class Solution:
    def kthLargest(self, N : int, K : int, Arr : List[int]) -> int:
        # code here
        Sum_arr = []
        Sum = 0
        
        for i in range(N):
            Sum = 0
            Sum_arr.append(Arr[i])
            Sum+=Arr[i]
            for j in range(i+1,N):
                Sum+=Arr[j]
                Sum_arr.append(Sum)
        Sum_arr.sort(reverse =True)
        # print(Sum_arr)
        return Sum_arr[K-1]



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        K = int(input())
        
        
        Arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.kthLargest(N, K, Arr)
        
        print(res)
        

# } Driver Code Ends