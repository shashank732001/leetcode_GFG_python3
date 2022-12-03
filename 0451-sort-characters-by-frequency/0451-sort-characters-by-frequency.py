class Solution:
    def frequencySort(self, s: str) -> str:
        lookup = {}
        s = sorted(s)
        for ch in s:
            lookup[ch]=1+lookup.get(ch,0)
    
        lookup_tup = sorted(lookup.items(),key=lambda x:x[1],reverse = True) 
        res = ""
        for key,val in lookup_tup:
            res = res+key*val
        
        return res