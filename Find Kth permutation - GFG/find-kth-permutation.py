from typing import List

import math
class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        # code here
        nums = [str(i+1) for i in range(n)]
        factorial = math.factorial(n)
        index = k-1
        out = []
        
        while nums:
            factorial = factorial//len(nums)
            pos = index//factorial
            ans = nums.pop(pos)
            out.append(ans)
            index = index%factorial
            
        return "".join(out)    
        
        
        
        
        
        
        # def perms(lookup,res):
            
        #     if len(res)==n:
        #         ans.append(res)
        #         return
            
        #     for i in nums:
        #         if i not in lookup:
        #             res+=i
        #             lookup.add(i)
        #             perms(lookup,res)
        #             lookup.remove(i)
        #             res =  res[:-1]
        #     return
                
        # ans = []
        # lookup = set()
        # n = len(nums)
        # res = ""
        # perms(lookup,res)
        # # print(ans) 
        # return ans[k-1]



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
        
        obj = Solution()
        res = obj.kthPermutation(a[0],a[1])
        
        print(res)
        

# } Driver Code Ends