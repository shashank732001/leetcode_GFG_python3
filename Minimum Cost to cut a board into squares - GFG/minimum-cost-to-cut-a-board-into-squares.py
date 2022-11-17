
from typing import List
class Solution:
    def minimumCostOfBreaking(self,X : List[int], Y : List[int],M : int, N : int) -> int:
        # code here
        X.sort(reverse=True)
        Y.sort(reverse=True)
        m = len(X)
        n = len(Y)
        ans = 0
        v_count = 1 #vertical count
        h_count = 1 #horizontal_count
        i = 0
        j = 0
        
        while i<m and j<n:
            if X[i]>Y[j]:
                ans+=X[i]*v_count
                h_count+=1
                i+=1
            
            else:
                ans+=Y[j]*h_count
                v_count+=1
                j+=1
        
        while i<m:
            ans+=X[i]*v_count
            h_count+=1
            i+=1
        
        while j<n:
            ans+=Y[j]*h_count
            v_count+=1
            j+=1
        
        return ans    
        
        



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
        
        a=IntArray().Input(2)
        m = a[0]
        n = a[1]
        
        tmp=IntArray().Input(a[0]-1) + IntArray().Input(a[1]-1)
        X = tmp[:m-1]
        Y = tmp[m-1:]
        
        obj = Solution()
        res = obj.minimumCostOfBreaking(X, Y,m,n)
        
        print(res)
        

# } Driver Code Ends