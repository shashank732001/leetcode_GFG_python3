class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        if k==0:
            return s
        
        elif k>1:
            return "".join(sorted(s))
        
        else:
            ans = s
            for i in range(len(s)):
                s = s[k:]+s[:k]
                ans = min(ans,s)
                # print(ans)
            return ans    
                
        
        