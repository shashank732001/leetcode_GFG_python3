from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        dp = [0]*n
        k = 2  # given only two transactions
        
        if k>n:
            A = [price[i]-price[i-1] for i in range(1,n)]
            return sum([b for b in A if b>0])
        
        for tns in range(k):
            pos = -price[0]
            profit = 0
            for i in range(1,n):
                pos = max(pos,dp[i]-price[i])
                profit = max(profit,pos+price[i])
                dp[i] = profit
        return dp[-1]
        
        
        



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
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends