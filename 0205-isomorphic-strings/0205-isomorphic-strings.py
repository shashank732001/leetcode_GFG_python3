class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup1 = {}
        lookup2 = {}
        
        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            
            if s[i] in lookup1:
                if lookup1[s[i]]!=t[i]:
                    return False
            else:
                lookup1[s[i]]=t[i]
                
        for i in range(len(s)):
            
            if t[i] in lookup2:
                if lookup2[t[i]]!=s[i]:
                    return False
            else:
                lookup2[t[i]]=s[i]       
        return True        