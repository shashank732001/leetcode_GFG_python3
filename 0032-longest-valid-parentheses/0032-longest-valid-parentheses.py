class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        char_stack = []
        stack.append(-1)
        ans  = 0
        
        for i in range(len(s)):
            if s[i]=="(":
                char_stack.append(s[i])
                stack.append(i)
            else:
                if char_stack:
                    char_stack.pop()
                    stack.pop()
                    ans = max(ans,i-stack[-1])
                else:
                    stack.append(i)
        return ans            
                    
                    
        