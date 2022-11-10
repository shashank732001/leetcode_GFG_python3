class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        if n==1:return s
        
        i = 0
        s = list(s)
        stack = []
        while i<len(s):
            if stack and s[i]==stack[-1]:
                stack.pop()
                s.pop(i)
            else:
                stack.append(s[i])
                i+=1
        return "".join(stack)       
            