
from typing import List
class Solution:
    def minimumSwaps(self,c : List[int], v : List[int],n : int,k : int,b : int, t : int) -> int:
        # code here
        swap = 0
        res = 0
        i = n-1
        while k>0 and i>=0:
            dist = v[i]*t
                
            if dist>=b-c[i]:
                res+=swap
                k-=1
                
            else:
                swap+=1
            i-=1
        if k>0:
            return -1
            
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
        
        a=IntArray().Input(4)
        n,k,b,t = a[0],a[1],a[2],a[3]
        
        c=IntArray().Input(a[0])
        
        
        v=IntArray().Input(a[0])
        
        obj = Solution()
        res = obj.minimumSwaps(c,v,n,k,b,t)
        
        print(res)
        

# } Driver Code Ends