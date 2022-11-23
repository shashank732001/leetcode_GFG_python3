class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        t = temperatures
        n = len(t)
        out = []
        
        for i in range(n-1,-1,-1):
            
            if not stack:
                out.append(0)
            
            elif stack and stack[-1][0]>t[i]:
                out.append(stack[-1][1]-i)
            
            else:
                while stack and stack[-1][0]<=t[i]:
                    stack.pop()
                
                if stack:
                    out.append(stack[-1][1]-i)
                
                else:
                    out.append(0)
            stack.append([t[i],i])  
        # print(out) 
        
        return out[::-1]
                    