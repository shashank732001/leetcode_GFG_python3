
from typing import List
class Solution:
    def findMinTime(self, n : int, l : int, arr : List[int]) -> int:
        # code here
        def ispossible(mid,n,arr):
            
            donuts = 0
            
            for t in arr:
                timetaken = 0
                timewilltake = t
                while timetaken+timewilltake<=mid:
                    donuts+=1
                    timetaken+=timewilltake
                    timewilltake+=t
            return donuts>=n       
        
        arr.sort()
        low = arr[0]
        high = arr[-1]*(n*(n+1))//2
        
        while low<=high:
            mid = (low+high)//2
            if ispossible(mid,n,arr):
                time = mid
                high = mid-1
            else:
                low = mid+1
        return time
        
        
        
        



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
        
        n = int(input())
        
        
        l = int(input())
        
        
        arr=IntArray().Input(l)
        
        obj = Solution()
        res = obj.findMinTime(n, l, arr)
        
        print(res)
        

# } Driver Code Ends