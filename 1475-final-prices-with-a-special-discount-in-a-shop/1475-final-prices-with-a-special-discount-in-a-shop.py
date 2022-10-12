class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        stack = []
        n = len(prices)
        
        for i in range(n-1,-1,-1):
            if not stack:
                res.append(prices[i])
            
            elif stack and stack[-1]<prices[i]:
                res.append(prices[i]-stack[-1])
                
            else:
                while stack and stack[-1]>prices[i]:
                    stack.pop()
                
                if stack:
                    res.append(prices[i]-stack[-1])
                
                else:
                    res.append(prices[i])
                    
            stack.append(prices[i])
        return res[::-1]    