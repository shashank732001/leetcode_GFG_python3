class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        res = []
        
        def subs(st,out):
            if st==n:
                res.append(out)
                return 
            
            for i in range(st,n):
                if s[st:i+1]==s[st:i+1][::-1]:
                    subs(i+1,out+[s[st:i+1]])
        
        subs(0,[])
        return res