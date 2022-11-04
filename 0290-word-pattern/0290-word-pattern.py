class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # pattern = [i for i in pattern]
        s = s.split()
        lookup1 = {}
        lookup2 = {}
        
        if len(s)!=len(pattern):
            return False
        
        for i in range(len(s)):
            if s[i] in lookup1:
                if lookup1[s[i]]!=pattern[i]:
                    return False
            else:
                lookup1[s[i]] = pattern[i]
                
        for i in range(len(s)):
            if pattern[i] in lookup2:
                if lookup2[pattern[i]]!=s[i]:
                    return False
            else:
                lookup2[pattern[i]] = s[i]        
        return True        