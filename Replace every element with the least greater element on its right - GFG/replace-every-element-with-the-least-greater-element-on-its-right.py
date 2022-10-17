
from bisect import bisect_right
from typing import List
class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        # code here
        
        s = []
        res = [-1]*n
        
        for i in range(n-1,-1,-1):
            ind = bisect_right(s,arr[i])
            # print(ind)
            if ind < len(s):
                res[i]=s[ind]

            s.insert(ind,arr[i])
        # print(v)
        return res
        



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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findLeastGreater(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends