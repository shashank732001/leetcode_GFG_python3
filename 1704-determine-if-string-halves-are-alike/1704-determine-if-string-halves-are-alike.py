class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2
        a = s[:mid]
        b = s[mid:]
        count1 = 0
        count2 = 0
        
        for i in range(mid):
            if a[i] in "aeiouAEIOU":
                count1+=1
                
            if b[i] in "aeiouAEIOU":
                count2+=1
        return count1==count2        
                