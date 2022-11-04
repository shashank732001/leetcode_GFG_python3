class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        cons = ""
        vows = ""
        ans = ""
        
        for i in s:
            if i.lower() in vowels:
                vows+=i
            else:
                cons+=i
                
        i = 0
        j = len(vows)-1
        
        for k in range(len(s)):
            if s[k].lower() in vowels:
                ans+=vows[j]
                j-=1
            else:
                ans+=cons[i]
                i+=1
        return ans        
                
                