class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for i in s:
            ind = t.find(i)
            if ind==-1:
                return False
            t = t[ind+1:]
        return True    
        
       