class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        n = len(s)
        lookup = set(wordDict)
        ans = []
        
        def func(start,out):
            
            
            if start==n:
                ans.append(out[:-1])
                return
            
            for j in range(start,n+1):
                if s[start:j] in lookup:
                    func(j,out+s[start:j]+" ")
       
        func(0,"")
        return ans 