class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            
            else:
                
                first = stack.pop()
                second = stack.pop()
                if i=="+":
                    new = second+first
                    stack.append(new)
                elif i =="-":
                    new = second-first
                    stack.append(new)
                elif i=="*":
                    new = second*first
                    stack.append(new)
                else:
                    new = second/first
                    stack.append(int(new))
        return stack[-1]            
                    