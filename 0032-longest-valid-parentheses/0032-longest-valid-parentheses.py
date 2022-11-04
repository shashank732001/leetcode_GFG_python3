class Solution:
    def longestValidParentheses(self, s: str) -> int:
#         stack = []
        
#         stack.append(-1)
#         ans  = 0
        
#         for i in range(len(s)):
#             if s[i]=="(":
                
#                 stack.append(i)
#             else:
#                 stack.pop()
#                 if not stack:
#                     stack.append(i)
                    
#                 else:
#                     ans = max(ans,i-stack[-1])
#         return ans 

        n = len(s)
        opened = 0
        closed = 0
        ans = 0
        
        for i in range(n):
            if s[i]=="(":
                opened+=1
            else:
                closed+=1
            
            if opened==closed:
                ans = max(ans,opened+closed)
            elif closed>opened:
                closed = 0
                opened = 0
                
        opened = 0
        closed = 0
        
        for i in range(n-1,-1,-1):
            if s[i]=="(":
                opened+=1
            else:
                closed+=1
            
            if opened==closed:
                ans = max(ans,opened+closed)
            elif opened>closed:
                opened = 0
                closed = 0
        return ans        
                
                
    
                    
                    
        